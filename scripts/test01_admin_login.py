from time import sleep
import allure
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
import page
from tool.get_logger import GetLogger
from tool.read_yaml import read_yaml

log = GetLogger.get_logger()


@pytest.fixture(autouse=True, scope="class")
def premise(browser):
    # 1.获取driver
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 2.通过统一入口类获取 管理员端-登录页面对象
    admin_login = PageIn(admin_driver).page_get_PageAdminLogin()
    # 3.获取医生列表页面对象
    admin_doctor_list = PageIn(admin_driver).page_get_PageAdminDoctorList()
    yield admin_login, admin_doctor_list

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminLogin:
    @allure.epic("管理员端")
    @allure.feature("登录用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.输入密码
        2.点击[登录]按钮
        3.如果密码错误，获取错误提示信息
        4.如果登录成功，获取系统log

    参数描述：
        1.password：密码
        2.expect：期望结果
        3.success：是否正向用例
        4.titles：用例标题
        """)
    # 业务方法--登录
    @pytest.mark.parametrize("password,expect,success,titles", read_yaml("admin", "scripts", "login.yaml"))
    def test_admin_login(self, password, expect, success, titles, premise):
        admin_login, admin_doctor_list = premise
        sleep(2)
        with allure.step("调用登录方法"):
            admin_login.page_admin_login(password)
        sleep(3)
        if success == "True":
            with allure.step("登录成功断言"):
                try:
                    assert admin_doctor_list.page_admin_doctor_list_get_log() == expect
                except AssertionError as e:
                    log.error("登录成功断言出错，错误信息：{}".format(e))
                    admin_login.base_get_image()
                    raise e

        else:
            with allure.step("登录失败断言"):
                try:
                    assert admin_login.page_admin_login_get_err() == expect
                except AssertionError as e:
                    log.error("登录失败断言出错，错误信息：{}".format(e))
                    admin_login.base_get_image()
                    raise e
