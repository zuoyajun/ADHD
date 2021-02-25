from time import sleep
import allure
import pytest
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_logger import GetLogger
from tool.read_yaml import read_yaml
from tool.redis_clear import redis_clear

log = GetLogger.get_logger()


@pytest.fixture(autouse=True, scope="class")
def premise(browser):
    # 1.获取driver
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 2.获取 登录页面对象
    admin_login = PageIn(admin_driver).page_get_PageAdminLogin()
    # 3.获取 忘记密码页面对象
    admin_login_porget_password = PageIn(admin_driver).page_get_PageAdminLoginPorgetPassword()
    # 4.获取 医生列表页面对象
    admin_doctor_list = PageIn(admin_driver).page_get_PageAdminDoctorList()
    yield admin_login, admin_login_porget_password, admin_doctor_list

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminLoginPorgetPassword:
    @allure.epic("管理员端")
    @allure.feature("忘记密码用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.点击[忘记密码]按钮，进入忘记密码①页面
        2.点击[获取验证码]按钮
        3.输入验证码
        3.如果验证码错误，获取错误提示信息并返回登录页面
        4.如果验证码超时，获取超时提示信息并返回登录页面
        5.如果验证码正确，进入忘记密码②页面
        6.输入新密码
        7.获取[设定新密码]按钮状态(是否可点击)
        8.如果[设定新密码]按钮不可点击，返回登录页面
        9.如果[设定新密码]按钮可点击，调用登录方法
        
    参数描述：
        1.code：验证码
        2.success：是否正向用例
        3.expiration：是否超时
        4.expect：期望结果
        5.new_password：新密码
        6.new_password_btn：设定新密码按钮状态
        7.restore：是否返回登录页面
        8.old_password：旧密码(还原使用)
        9.time：等待时间
        10.titles：用例标题
            """)
    # 业务方法--忘记密码+还原
    @pytest.mark.parametrize("code,success,expiration,expect,new_password,"
                             "new_password_btn,restore,old_password,time,titles",
                             read_yaml("admin", "scripts", "login_porget_password.yaml"))
    def test_admin_login_porget_password(self, code,
                                         success,
                                         expiration,
                                         expect,
                                         new_password,
                                         new_password_btn,
                                         restore,
                                         old_password,
                                         time,
                                         titles,
                                         premise):
        admin_login, admin_login_porget_password, admin_doctor_list = premise

        sleep(2)
        # 获取邮箱
        email = admin_login.page_admin_login_get_email()
        redis_clear(email)
        with allure.step("点击忘记密码按钮"):
            admin_login.page_admin_login_porget_password()
            sleep(2)
        with allure.step("点击获取验证码按钮"):
            admin_login_porget_password.page_admin_login_porget_password_get_code_btn()
            sleep(5)
        if success == "True":
            with allure.step("输入验证码"):
                admin_login_porget_password.page_admin_login_porget_password_input_code(code)
                sleep(1)
            with allure.step("输入新密码"):
                admin_login_porget_password.page_admin_login_porget_password_new_input(new_password)
                sleep(1)
            with allure.step("断言设定新密码按钮状态"):
                try:
                    assert admin_login_porget_password.page_admin_login_porget_password_new_btn_is_enabled() == eval(
                        new_password_btn)
                except AssertionError as e:
                    log.error("设定新密码按钮状态，断言错误，错误信息：{}".format(e))
                    admin_login_porget_password.base_get_image()
                    raise e

            if new_password_btn == "True":
                sleep(1)
                with allure.step("点击设定新密码按钮"):
                    admin_login_porget_password.page_admin_login_porget_password_new_btn()
                    sleep(1)
                with allure.step("调用登录方法"):
                    admin_login.page_admin_login(new_password)
                    sleep(3)
                with allure.step("登录成功断言"):
                    try:
                        assert admin_doctor_list.page_admin_doctor_list_get_log() == expect
                    except AssertionError as e:
                        log.error("登录成功断言出错，错误信息：{}".format(e))
                        admin_login.base_get_image()
                        raise e
                    sleep(1)
                with allure.step("点击浏览器后退按钮->回到登录页面"):
                    admin_login_porget_password.base_driver_back()
                    sleep(1)
            else:
                with allure.step("点击返回登录按钮"):
                    admin_login_porget_password.page_admin_login_porget_return_login()
                    sleep(1)

        else:
            if expiration == "True":
                sleep(60)
                with allure.step("等60秒输入验证码"):
                    admin_login_porget_password.page_admin_login_porget_password_input_code(code)
                    sleep(2)
            else:
                with allure.step("输入验证码"):
                    admin_login_porget_password.page_admin_login_porget_password_input_code(code)
                    sleep(2)
            with allure.step("断言验证码超时提示信息"):
                try:
                    assert admin_login_porget_password.page_admin_login_porget_password_get_err() == expect
                except AssertionError as e:
                    log.error("验证码超时提示信息,断言错误，错误信息：{}".format(e))
                    admin_login_porget_password.base_get_image()
                    raise e
                sleep(1)
            with allure.step("点击返回登录按钮"):
                admin_login_porget_password.page_admin_login_porget_return_login()
                sleep(1)

        if restore == "True":
            sleep(60)
            with allure.step("点击忘记密码按钮"):
                admin_login.page_admin_login_porget_password()
                sleep(1)
            with allure.step("调用忘记密码方法(还原)"):
                admin_login_porget_password.page_admin_login_porget_password_group(code, old_password)
            with allure.step("清除redis"):
                redis_clear(email)
        with allure.step("等待{}秒".format(eval(time))):
            sleep(eval(time))
