from time import sleep
import allure
import pytest
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_logger import GetLogger
from tool.get_mysql import *
from tool.read_yaml import read_yaml

log = GetLogger.get_logger()


@pytest.fixture(autouse=True, scope="class")
def premise(browser):
    # 1.获取driver
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 2.调用 管理员端-成功登录依赖方法
    PageIn(admin_driver).page_get_PageAdminLogin().page_admin_login_success()
    # 3.获取 管理员端-创建医生页面对象
    admin_create_doctor = PageIn(admin_driver).page_get_PageAdminCreateDoctor()
    # 4.获取 管理员端-医生列表页面对象
    admin_doctor_list = PageIn(admin_driver).page_get_PageAdminDoctorList()
    # 5.获取 管理员端-医生详情对象
    admin_doctor_detail = PageIn(admin_driver).page_get_PageAdminDoctorDetail()
    yield admin_create_doctor, admin_doctor_list, admin_doctor_detail

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminCreateDoctor:
    @allure.epic("管理员端")
    @allure.feature("创建医生用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.调用登录方法
        2.点击[创建医生]按钮
        3.输入医生姓名
        4.如果身份证号错误，获取错误提示信息
        5.如果身份证号已存在，获取已存在提示信息
        6.如果身份证号正确，成功创建并去医生详情页验证
        7.删除创建的数据
        
    参数描述：
        1.doctor_status：账号状态(是否激活)
        2.doctor_name：姓名
        3.doctor_sex：性别
        4.doctor_num：身份证号
        5.expect：期望结果
        6.doctor_no_phone：手机号
        7.doctor_unit：单位
        8.doctor_create_time：创建时间
        9.success：是否正向用例
        10.is_delete：是否删除
        11.doctor_create_delete_relevance：删除关联sql
        12.doctor_create_delete：删除数据sql
        13.titles：用例标题
            """)
    # 业务方法--创建医生
    @pytest.mark.parametrize(
        "doctor_status,doctor_name,doctor_sex,doctor_num,expect,doctor_no_phone,doctor_unit,"
        "doctor_create_time,success,is_delete,doctor_create_delete_relevance,doctor_create_delete,titles",
        read_yaml("admin", "scripts", "create_doctor.yaml"))
    def test_admin_create_doctor(self, doctor_status,
                                 doctor_name,
                                 doctor_sex,
                                 doctor_num,
                                 expect,
                                 doctor_no_phone,
                                 doctor_unit,
                                 doctor_create_time,
                                 success,
                                 is_delete,
                                 doctor_create_delete_relevance,
                                 doctor_create_delete,
                                 titles,
                                 premise):
        admin_create_doctor, admin_doctor_list, admin_doctor_detail = premise
        sleep(2)
        with allure.step("调用创建医生方法"):
            admin_create_doctor.page_admin_create_doctor(doctor_name, doctor_num)
        sleep(2)
        if success == "True":
            with allure.step("点击医生列表第一个医生的详情按钮"):
                admin_doctor_list.page_admin_doctor_list_click_first_doctor_detail()
            sleep(2)

            with allure.step("账号状态断言"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_status() == doctor_status
                except AssertionError as e:
                    log.error("医生状态断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            with allure.step("姓名断言"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_name() == doctor_name
                except AssertionError as e:
                    log.error("医生姓名断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            with allure.step("性别断言"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_grt_sex() == doctor_sex
                except AssertionError as e:
                    log.error("医生性别断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            with allure.step("身份证号断言"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_num() == doctor_num
                except AssertionError as e:
                    log.error("身份证号断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            with allure.step("未激活手机号断言"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_no_phone() == doctor_no_phone
                except AssertionError as e:
                    log.error("未激活手机号断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            with allure.step("单位断言"):
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_unit() == doctor_unit
                except AssertionError as e:
                    log.error("单位断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            with allure.step("创建时间断言"):
                create_time = get_select_mysql(doctor_create_time)
                log.info("数据库查询创建时间为：{}".format(create_time))
                try:
                    assert admin_doctor_detail.page_admin_doctor_detail_get_create_time() == create_time[0][0]
                except AssertionError as e:
                    log.error("创建时间断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            sleep(1)
            with allure.step("点击医生列表"):
                admin_doctor_list.page_admin_doctor_list_btn()

        else:
            sleep(1)
            with allure.step("创建医生失败断言"):
                try:
                    assert admin_create_doctor.page_admin_create_doctor_get_err() == expect
                except AssertionError as e:
                    log.error("错误提示断言出错，错误信息：{}".format(e))
                    admin_create_doctor.base_get_image()
                    raise e
            with allure.step("关闭创建医生弹窗"):
                admin_create_doctor.page_admin_create_doctor_close()

        if is_delete == "True":
            with allure.step("删除创建的数据"):
                get_mysql(doctor_create_delete_relevance)
                log.info("删除关联")
                get_mysql(doctor_create_delete)
                log.info("删除创建的数据")
