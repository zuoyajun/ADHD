from time import sleep
import page
from base.base import Base


class PageAdminLoginPorgetPassword(Base):
    # 点击返回登录页面按钮
    def page_admin_login_porget_return_login(self):
        self.base_click(page.admin_login_porget_password_login_btn)

    # 点击获取验证码按钮
    def page_admin_login_porget_password_get_code_btn(self):
        self.base_click(page.admin_login_porget_password_get_code)

    # 输入验证码[1]
    def page_admin_login_porget_password_input_code1(self, code1):
        self.base_input(page.admin_login_porget_password_input_code1, code1)

    # 输入验证码[2]
    def page_admin_login_porget_password_input_code2(self, code1):
        self.base_input(page.admin_login_porget_password_input_code2, code1)

    # 输入验证码[3]
    def page_admin_login_porget_password_input_code3(self, code3):
        self.base_input(page.admin_login_porget_password_input_code3, code3)

    # 输入验证码[4]
    def page_admin_login_porget_password_input_code4(self, code4):
        self.base_input(page.admin_login_porget_password_input_code4, code4)

    # 输入验证码
    def page_admin_login_porget_password_input_code(self, code):
        self.page_admin_login_porget_password_input_code1(code[0])
        sleep(0.5)
        self.page_admin_login_porget_password_input_code2(code[1])
        sleep(0.5)
        self.page_admin_login_porget_password_input_code3(code[2])
        sleep(0.5)
        self.page_admin_login_porget_password_input_code4(code[3])

    # 获取验证码提示信息
    def page_admin_login_porget_password_get_err(self):
        return self.base_get_text(page.admin_login_porget_password_get_err)

    # 输入新密码
    def page_admin_login_porget_password_new_input(self, new_password):
        self.base_input(page.admin_login_porget_password_new_input, new_password)

    # 判断设定新密码按钮是否可用
    def page_admin_login_porget_password_new_btn_is_enabled(self):
        return self.base_is_enabled(page.admin_login_porget_password_new_btn)

    # 点击设定新密码按钮
    def page_admin_login_porget_password_new_btn(self):
        self.base_click(page.admin_login_porget_password_new_btn)

    # 组合业务方法——忘记密码-->还原使用
    def page_admin_login_porget_password_group(self, code, new_password):
        self.page_admin_login_porget_password_get_code_btn()
        sleep(3)
        self.page_admin_login_porget_password_input_code(code)
        sleep(1)
        self.page_admin_login_porget_password_new_input(new_password)
        sleep(1)
        self.page_admin_login_porget_password_new_btn()
        sleep(1)
