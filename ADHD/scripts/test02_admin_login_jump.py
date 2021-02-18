from time import sleep
import allure
import pytest
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_logger import GetLogger
from tool.read_yaml import read_yaml

log = GetLogger.get_logger()


@pytest.fixture(autouse=True, scope="class")
def premise(browser):
    # 1.获取管理员端driver
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 2.获取管理员端-登录页面对象
    admin_login = PageIn(admin_driver).page_get_PageAdminLogin()
    # 3.获取医生端-登陆页面对象
    doctor_login = PageIn(admin_driver).page_get_PageDoctorLogin()
    yield admin_login, doctor_login

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminLoginJump:
    @allure.epic("管理员端")
    @allure.feature("跳转用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.点击[医生登录]按钮
        2.跳转到医生端登录页面，获取医生端log
        3.点击[管理员登录]按钮
        4.跳转到管理员端登录页面，获取管理员端log
        
    参数描述：
        1.login：开始页面
        2.expect：期望结果
        3.titles：用例标题
        """)
    # 业务方法--登录页面跳转
    @pytest.mark.parametrize("login,expect,titles", read_yaml("admin", "scripts", "login_jump.yaml"))
    def test_admin_login_jump(self, login, expect, titles, premise):
        admin_login, doctor_login = premise
        sleep(2)
        if login == "admin":
            with allure.step("点击医生登录按钮"):
                admin_login.page_admin_login_doctor_btn()
            sleep(1)
            with allure.step("成功跳转医生登录页面断言"):
                try:
                    assert doctor_login.page_doctor_login_get_log() == expect
                except AssertionError as e:
                    log.error("成功跳转医生登录页面断言出错，错误信息：{}".format(e))
                    doctor_login.base_get_image()
                    raise e
        else:
            with allure.step("点击管理员登录按钮"):
                doctor_login.page_doctor_login_admin_btn()
            sleep(1)
            with allure.step("成功跳转管理员登录页面断言"):
                try:
                    assert admin_login.page_admin_login_get_log() == expect
                except AssertionError as e:
                    log.error("成功跳转管理员登录页面断言出错，错误信息：{}".format(e))
                    admin_login.base_get_image()
                    raise e
