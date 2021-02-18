from time import sleep
import allure
import pytest
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_logger import GetLogger
from tool.get_mysql import get_mysql
from tool.read_yaml import read_yaml

log = GetLogger.get_logger()


@pytest.fixture(autouse=True, scope="class")
def premise(browser):
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 调用登录方法
    PageIn(admin_driver).page_get_PageAdminLogin().page_admin_login_success()
    # 获取创建医生页面对象
    admin_create_doctor = PageIn(admin_driver).page_get_PageAdminCreateDoctor()
    # 获取医生列表页面对象
    admin_doctor_list = PageIn(admin_driver).page_get_PageAdminDoctorList()
    # 获取医生详情页面对象
    admin_doctor_detail = PageIn(admin_driver).page_get_PageAdminDoctorDetail()
    yield admin_create_doctor, admin_doctor_list, admin_doctor_detail

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminDoctorDetailFrozen:
    @allure.epic("管理员端")
    @allure.feature("医生详情用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.调用登录方法
        2.调用创建医生方法
        3.数据库激活
        4.冻结医生
        5.获取冻结状态并断言
        6.解除冻结
        7.获取冻结医生按钮文本并断言

    参数描述：
        1.doctor_name：创建医生的姓名
        2.doctor_num：创建医生的身份证号
        3.mysql_activate：激活账号sql
        4.expect：期望结果
        5.doctor_create_delete_relevance：删除关联sql
        6.doctor_create_delete：删除数据sql
        7.titles：用例标题
        """)
    # 业务方法--医生详情(冻结医生)
    @pytest.mark.parametrize("doctor_name,doctor_num,mysql_activate,expect,"
                             "doctor_create_delete_relevance,doctor_create_delete,titles",
                             read_yaml("admin", "scripts", "doctor_detail_frozen.yaml"))
    def test_admin_doctor_detail_frozen(self, doctor_name,
                                        doctor_num,
                                        mysql_activate,
                                        expect,
                                        doctor_create_delete_relevance,
                                        doctor_create_delete,
                                        titles,
                                        premise):
        admin_create_doctor, admin_doctor_list, admin_doctor_detail = premise

        with allure.step("调用创建医生方法"):
            admin_create_doctor.page_admin_create_doctor(doctor_name, doctor_num)
        sleep(1)
        with allure.step("数据库修改状态为激活"):
            get_mysql(mysql_activate)
            log.info("账号激活，身份证号为：{}".format(doctor_num))

        sleep(2)
        with allure.step("点击医生列表第一个医生的详情按钮"):
            admin_doctor_list.page_admin_doctor_list_click_first_doctor_detail()
        sleep(1)
        with allure.step("获取冻结医生按钮文本"):
            frozen_text = admin_doctor_detail.page_admin_doctor_detail_frozen_get_text()
        with allure.step("点击冻结医生按钮"):
            admin_doctor_detail.page_admin_doctor_detail_frozen_click()
        sleep(1)
        with allure.step("点击冻结按钮"):
            admin_doctor_detail.page_admin_doctor_detail_pop_frozen_click()
            sleep(2)
            with allure.step("断言冻结状态"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_frozen_status_get_text() == expect
                except AssertionError as e:
                    log.error("冻结状态断言出错，错误信息：{}".format(e))
                    admin_doctor_detail.base_get_image()
                    raise e
        with allure.step("点击解除冻结按钮"):
            admin_doctor_detail.page_admin_doctor_detail_unfreeze_click()
        sleep(1)
        with allure.step("点击解冻按钮"):
            admin_doctor_detail.page_admin_doctor_detail_pop_unfreeze_click()
            sleep(1)
            with allure.step("断言解冻状态"):
                try:
                    assert frozen_text == admin_doctor_detail.page_admin_doctor_detail_frozen_get_text()
                except AssertionError as e:
                    log.error("解除冻结断言出错，错误信息：{}".format(e))
                    admin_doctor_detail.base_get_image()
                    raise e
        with allure.step("删除创建的数据"):
            get_mysql(doctor_create_delete_relevance)
            log.info("删除关联")
            get_mysql(doctor_create_delete)
            log.info("删除创建的数据")
