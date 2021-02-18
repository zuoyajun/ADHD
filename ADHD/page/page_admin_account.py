from time import sleep
import page
from base.base import Base


class PageAdminAccount(Base):
    # 获取邮箱
    def page_account_get_email(self):
        return self.base_get_text(page.admin_account_get_email)[:-3]

    # 点击邮箱修改按钮
    def page_account_email_change_btn(self):
        self.base_click(page.admin_account_email_change)

    # 点击获取邮箱验证码按钮
    def page_account_pop_get_code(self):
        self.base_click(page.admin_account_pop_get_code)

    # 验证码输入框1
    def page_account_pop_code_input1(self, code1):
        self.base_input(page.admin_account_pop_code_input1, code1)

    # 验证码输入框2
    def page_account_pop_code_input2(self, code2):
        self.base_input(page.admin_account_pop_code_input2, code2)

    # 验证码输入框3
    def page_account_pop_code_input3(self, code3):
        self.base_input(page.admin_account_pop_code_input3, code3)

    # 验证码输入框4
    def page_account_pop_code_input4(self, code4):
        self.base_input(page.admin_account_pop_code_input4, code4)

    # 验证码输入框
    def page_account_pop_code_input(self, code):
        self.page_account_pop_code_input1(code[0])
        sleep(0.5)
        self.page_account_pop_code_input2(code[1])
        sleep(0.5)
        self.page_account_pop_code_input3(code[2])
        sleep(0.5)
        self.page_account_pop_code_input4(code[3])

    # 错误提示信息
    def page_account_pop_get_err(self):
        return self.base_get_text(page.admin_account_pop_get_err)

    # 关闭弹窗
    def page_account_pop_close(self):
        self.base_click(page.admin_account_pop_close)

    # 修改邮箱-新邮箱输入框
    def page_account_pop_new_email_input(self, new_email):
        self.base_send_input(page.admin_account_pop_new_email_input, new_email)

    # 点击密码修改按钮
    def page_account_password_change(self):
        self.base_click(page.admin_account_password_change)

    # 修改密码-关闭弹窗
    def page_account_pop_change_password_close(self):
        self.base_click(page.admin_account_pop_change_password_close)

    # 退出登录
    def page_account_login_out(self):
        self.base_click(page.admin_account_login_out_btn)
        sleep(1)
        self.base_click(page.admin_account_pop_out_btn)
