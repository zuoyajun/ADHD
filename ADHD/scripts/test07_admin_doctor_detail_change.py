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
class TestAdminDoctorDetailChange:
    @allure.epic("管理员端")
    @allure.feature("医生详情用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.调用登录方法
        2.调用创建医生方法
        3.修改姓名
        4.修改手机号
        5.如果手机号已存在，则对提示信息进行校验,并关闭弹窗
        6.修改备注

    参数描述：
        1.doctor_name：创建医生的姓名
        2.doctor_num：创建医生的身份证号
        3.mysql_activate：激活账号sql
        4.change_name：修改的姓名
        5.change_phone：修改的手机号
        6.change_phone_success：是否成功修改
        7.pop_phone_expect：手机号已存在提示信息
        8.change_remark：修改的备注
        9.doctor_create_delete_relevance：删除关联sql
        10.doctor_create_delete：删除数据sql
        11.titles：用例标题
        """)
    # 业务方法--医生详情(修改)
    @pytest.mark.parametrize("doctor_name,doctor_num,mysql_activate,change_name,change_phone,"
                             "change_phone_success,pop_phone_expect,change_remark,"
                             "doctor_create_delete_relevance,doctor_create_delete,titles",
                             read_yaml("admin", "scripts", "doctor_detail_change.yaml"))
    def test_admin_doctor_detail_change(self, doctor_name,
                                        doctor_num,
                                        mysql_activate,
                                        change_name,
                                        change_phone,
                                        change_phone_success,
                                        pop_phone_expect,
                                        change_remark,
                                        doctor_create_delete_relevance,
                                        doctor_create_delete,
                                        titles,
                                        premise):
        admin_create_doctor, admin_doctor_list, admin_doctor_detail = premise

        sleep(2)
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

        with allure.step("修改医生姓名"):
            admin_doctor_detail.page_admin_doctor_detail_change_name(change_name)
            with allure.step("断言修改的医生姓名"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_name() == change_name
                except AssertionError as e:
                    log.error("修改医生姓名，断言出错，错误信息：{}".format(e))
                    admin_doctor_detail.base_get_image()
                    raise e
            sleep(1)

        with allure.step("修改医生手机号"):
            admin_doctor_detail.page_admin_doctor_detail_change_phone(change_phone)
            if change_phone_success == "True":
                with allure.step("断言修改的手机号"):
                    try:
                        assert admin_doctor_detail.page_admin_doctor_detail_get_yes_phone() == change_phone
                    except AssertionError as e:
                        log.error("获取手机号，断言出错，错误信息：{}".format(e))
                        admin_doctor_detail.base_get_image()
                        raise e
                sleep(1)
            else:
                with allure.step("断言手机号已存在"):
                    try:
                        assert admin_doctor_detail.page_admin_doctor_detail_pop_get_err() == pop_phone_expect
                    except AssertionError as e:
                        log.error("手机号弹窗错误提示信息，断言出错，错误信息：{}".format(e))
                        admin_doctor_detail.base_get_image()
                        raise e
                with allure.step("修改手机号-关闭弹窗"):
                    admin_doctor_detail.page_admin_doctor_detail_pop_phone_close()
                sleep(1)

        with allure.step("修改备注"):
            admin_doctor_detail.page_admin_doctor_detail_change_remark(change_remark)
            with allure.step("断言修改的备注"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_remark() == change_remark
                except AssertionError as e:
                    log.error("备注文本信息，断言出错，错误信息：{}".format(e))
                    admin_doctor_detail.base_get_image()
                    raise e
        sleep(1)
        with allure.step("删除创建的数据"):
            get_mysql(doctor_create_delete_relevance)
            log.info("删除关联")
            get_mysql(doctor_create_delete)
            log.info("删除创建的数据")
        sleep(1)
        with allure.step("点击医生列表"):
            admin_doctor_list.page_admin_doctor_list_btn()
