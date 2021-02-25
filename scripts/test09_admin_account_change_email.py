from time import sleep
import allure
import pytest
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_logger import GetLogger
from tool.get_mysql import get_mysql
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
    yield admin_account

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminAccountChangeEmail:
    @allure.epic("管理员端")
    @allure.feature("管理员账户用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.调用登录方法
        2.调用点击账户按钮方法
        3.点击邮箱后面的[修改]按钮
        4.点击[获取邮箱验证码]按钮
        5.输入验证码
        6.如果验证码错误，获取错误提示信息并关闭弹窗
        7.如果验证码超时，获取超时提示信息并关闭弹窗
        8.如果验证码正确，进入修改邮箱页面
        9.输入新邮箱
        10.如果输入的新邮箱不符合规则，点击[获取邮箱验证码]按钮，获取错误信息并关闭弹窗
        11.如果输入的新邮箱符合规则，点击[获取邮箱验证码]按钮
        12.输入新邮箱验证码
        13.如果验证码错误，获取错误提示信息并关闭弹窗
        14.如果验证码超时，获取超时提示信息并关闭弹窗
        15.如果验证码正确，成功修改并还原

    参数描述：
        1.identity：身份验证页面-是否通过
        2.identity_timeout：身份验证页面-验证码是否超时
        3.identity_code：身份验证页面-验证码
        4.expect：预期结果
        5.new_email：修改邮箱页面-新邮箱
        6.new_email_true：新邮箱是否符合规则
        7.change_email：修改邮箱页面-是否通过
        8.restore_sql：还原sql
        9.email_timeout：修改邮箱页面-验证码是否超时
        10.email_code：修改邮箱页面-验证码
        11.time: 等待时间
        12.titles：用例标题
        """)
    # 业务方法--账户(修改邮箱+还原)
    @pytest.mark.parametrize("identity,identity_timeout,identity_code,expect,new_email,new_email_true,"
                             "change_email,restore_sql,email_timeout,email_code,time,titles",
                             read_yaml("admin", "scripts", "account_change_email.yaml"))
    def test_admin_account_change_email(self,
                                        identity,
                                        identity_timeout,
                                        identity_code,
                                        expect,
                                        new_email,
                                        new_email_true,
                                        change_email,
                                        restore_sql,
                                        email_timeout,
                                        email_code,
                                        time,
                                        titles,
                                        premise):
        admin_account = premise
        sleep(1)
        # 调用 获取邮箱方法
        old_email = admin_account.page_account_get_email()
        redis_clear(old_email)
        redis_clear(new_email)
        with allure.step("点击邮箱-修改按钮"):
            admin_account.page_account_email_change_btn()
        sleep(1)
        with allure.step("身份验证-点击获取邮箱验证码按钮"):
            admin_account.page_account_pop_get_code()
        sleep(5)

        if identity == "True":
            with allure.step("身份验证-输入验证码"):
                admin_account.page_account_pop_code_input(identity_code)
            sleep(2)
            with allure.step("修改邮箱-输入新邮箱"):
                admin_account.page_account_pop_new_email_input(new_email)
            sleep(1)
            with allure.step("修改邮箱-点击获取邮箱验证码按钮"):
                admin_account.page_account_pop_get_code()
            sleep(8)
            if new_email_true == "True":
                if change_email == "True":
                    with allure.step("修改邮箱-输入验证码"):
                        admin_account.page_account_pop_code_input(email_code)
                        sleep(2)
                    with allure.step("断言修改的邮箱"):
                        try:
                            assert admin_account.page_account_get_email() == new_email
                        except AssertionError as e:
                            log.error("获取的邮箱与输入的邮箱，断言出错，错误信息：{}".format(e))
                            admin_account.base_get_image()
                            raise e
                    with allure.step("还原修改的邮箱"):
                        get_mysql(restore_sql.format(old_email))

                else:
                    if email_timeout == "True":
                        sleep(60)
                        with allure.step("等待60秒，修改邮箱-输入验证码"):
                            admin_account.page_account_pop_code_input(email_code)
                            sleep(2)
                            with allure.step("断言验证码超时"):
                                try:
                                    assert admin_account.page_account_pop_get_err() == expect
                                except AssertionError as e:
                                    log.error("验证码超时提示信息，断言出错，错误信息：{}".format(e))
                                    admin_account.base_get_image()
                                    raise e
                    else:
                        with allure.step("修改邮箱-输入验证码"):
                            admin_account.page_account_pop_code_input(email_code)
                            sleep(2)
                            with allure.step("断言验证码错误提示信息"):
                                try:
                                    assert admin_account.page_account_pop_get_err() == expect
                                except AssertionError as e:
                                    log.error("验证码错误提示信息，断言出错，错误信息：{}".format(e))
                                    admin_account.base_get_image()
                                    raise e
                    with allure.step("修改邮箱-关闭弹窗"):
                        admin_account.page_account_pop_close()
                    sleep(1)

            else:
                with allure.step("断言邮箱错误提示信息"):
                    try:
                        assert admin_account.page_account_pop_get_err() == expect
                    except AssertionError as e:
                        log.error("邮箱错误提示信息，断言出错，错误信息：{}".format(e))
                        admin_account.base_get_image()
                        raise e
                with allure.step("修改邮箱-关闭弹窗"):
                    admin_account.page_account_pop_close()
                sleep(1)

        else:
            if identity_timeout == "True":
                sleep(60)
                with allure.step("等待60秒，身份验证-输入验证码"):
                    admin_account.page_account_pop_code_input(identity_code)
                    sleep(2)
                    with allure.step("断言验证码超时"):
                        try:
                            assert admin_account.page_account_pop_get_err() == expect
                        except AssertionError as e:
                            log.error("身份验证-验证码超时提示信息，断言出错，错误信息：{}".format(e))
                            admin_account.base_get_image()
                            raise e
            else:
                with allure.step("身份验证-输入验证码"):
                    admin_account.page_account_pop_code_input(identity_code)
                    sleep(2)
                    with allure.step("断言验证码错误提示信息"):
                        try:
                            assert admin_account.page_account_pop_get_err() == expect
                        except AssertionError as e:
                            log.error("身份验证-验证码错误提示信息，断言出错，错误信息：{}".format(e))
                            admin_account.base_get_image()
                            raise e

            with allure.step("身份验证-关闭弹窗"):
                admin_account.page_account_pop_close()
            sleep(1)
        with allure.step("清除redis"):
            redis_clear(old_email)
            redis_clear(new_email)
        with allure.step("等待{}秒".format(eval(time))):
            sleep(eval(time))
