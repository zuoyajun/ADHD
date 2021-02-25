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
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 调用 成功登录方法
    PageIn(admin_driver).page_get_PageAdminLogin().page_admin_login_success()
    # 调用 点击账户按钮方法
    PageIn(admin_driver).page_get_PageAdminDoctorList().page_admin_doctor_list_account()
    # 调用 账户页面对象
    admin_account = PageIn(admin_driver).page_get_PageAdminAccount()
    # 调用 忘记密码页面对象
    admin_login_porget_password = PageIn(admin_driver).page_get_PageAdminLoginPorgetPassword()
    # 调用 登录页面对象
    admin_login = PageIn(admin_driver).page_get_PageAdminLogin()
    # 调用 医生列表页面对象
    admin_doctor_list = PageIn(admin_driver).page_get_PageAdminDoctorList()
    yield admin_account, admin_login_porget_password, admin_login, admin_doctor_list

    admin_driver.quit()


# 跳过用例
@pytest.mark.skipif(reason="暂不使用")
class TestAdminAccountChangePassword:
    @allure.epic("管理员端")
    @allure.feature("管理员账户用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.调用登录方法
        2.调用点击账户按钮方法
        3.点击密码后面的[修改]按钮
        4.点击[获取邮箱验证码]按钮
        5.输入验证码
        6.如果验证码正确，进入修改密码页面
        7.输入密码
        8.获取[设定新密码]按钮状态(是否可点击)
        9.如果[设定新密码]按钮不可点击，关闭弹窗
        10.如果[设定新密码]按钮可点击，点击退出登录
        11.调用登录方法，并还原密码

    参数描述：
        1.identity_code：身份验证页面-验证码
        2.new_password：
        3.new_password_btn：设定新密码按钮是否激活
        4.expect：登录成功预期结果
        5.time：等待时间
        6.titles：用例标题
        """)
    # 业务方法--账户(修改密码 + 还原)
    @pytest.mark.parametrize("identity_code,new_password,new_password_btn,expect,titles",
                             read_yaml("admin", "scripts", "account_change_password.yaml"))
    def test_admin_account_change_password(self, identity_code,
                                           new_password,
                                           new_password_btn,
                                           expect,
                                           titles,
                                           premise):
        admin_account, admin_login_porget_password, admin_login, admin_doctor_list = premise
        # 调用 获取邮箱方法
        email = admin_account.page_account_get_email()
        redis_clear(email)
        sleep(1)
        with allure.step("点击密码-修改按钮"):
            admin_account.page_account_password_change()
        sleep(1)
        with allure.step("身份验证-点击获取邮箱验证码按钮"):
            admin_account.page_account_pop_get_code()
        sleep(5)
        with allure.step("身份验证-输入验证码"):
            admin_account.page_account_pop_code_input(identity_code)
        sleep(2)
        with allure.step("输入新密码"):
            admin_login_porget_password.page_admin_login_porget_password_new_input(new_password)
        sleep(3)
        if new_password_btn == "True":
            with allure.step("点击设定新密码按钮"):
                admin_login_porget_password.page_admin_login_porget_password_new_btn()
            sleep(2)
            with allure.step("调用登录方法"):
                admin_login.page_admin_login(new_password)
            sleep(1)
            with allure.step("登录成功断言"):
                try:
                    assert admin_doctor_list.page_admin_doctor_list_get_log() == expect
                except AssertionError as e:
                    log.error("登录成功断言出错，错误信息：{}".format(e))
                    admin_login.base_get_image()
                    raise e
            with allure.step("清除redis"):
                redis_clear(email)
        else:
            with allure.step("断言设定新密码按钮状态"):
                try:
                    assert admin_login_porget_password.page_admin_login_porget_password_new_btn_is_enabled() == eval(
                        new_password_btn)
                except AssertionError as e:
                    log.error("设定新密码按钮状态断言错误，错误信息：{}".format(e))
                    admin_login_porget_password.base_get_image()
                    raise e
            with allure.step("修改密码-关闭弹窗"):
                admin_account.page_account_pop_change_password_close()

            with allure.step("等待60秒"):
                sleep(60)
