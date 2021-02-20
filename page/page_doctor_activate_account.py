from time import sleep
import page
from base.base import Base


class PageDoctorActivateAccount(Base):
    # 点击去激活账号按钮
    def page_doctor_activate_account_btn(self):
        self.base_click(page.doctor_activate_account_btn)

    # 返回登录按钮
    def page_doctor_activate_account_return_login(self):
        self.base_click(page.doctor_activate_return_login)

    # 激活账号①页面-输入姓名
    def page_doctor_activate_account_name_input(self, name):
        self.base_input(page.doctor_activate_name, name)

    # 激活账号①页面-输入身份证号
    def page_doctor_activate_account_num_input(self, num):
        self.base_input(page.doctor_activate_num, num)

    # 激活账号①页面-点击下一步按钮
    def page_doctor_activate_account_next_step_click(self):
        self.base_click(page.doctor_activate_next_step)

    # 激活账号①页面-获取账号提示信息
    def page_doctor_activate_account_get_account_err(self):
        return self.base_get_text(page.doctor_activate_get_account_err)

    # 激活账号②页面-输入手机号
    def page_doctor_activate_account_phone_input(self, phone):
        self.base_input(page.doctor_activate_phone, phone)

    # 激活账号②页面-判断获取验证码按钮是否可用
    def page_doctor_activate_account_get_code_btn_is_enabled(self):
        self.base_is_enabled(page.doctor_activate_get_code_btn)

    # 激活账号②页面-点击获取验证码按钮
    def page_doctor_activate_account_get_code(self):
        self.base_click(page.doctor_activate_get_code_btn)

    # 激活账号②页面-输入验证码
    def page_doctor_activate_account_code_input(self, code):
        self.base_input(page.doctor_activate_code_input, code)

    # 激活账号②页面-获取验证码提示信息
    def page_doctor_activate_account_get_code_err(self):
        return self.base_get_text(page.doctor_account_get_code_err)

    # 激活账号③页面-输入新密码
    def page_doctor_activate_account_new_password_input(self, new_password):
        self.base_input(page.doctor_activate_new_password_input, new_password)

    # 激活账号③页面-判断设定新密码按钮是否可用
    def page_doctor_activate_account_new_password_btn_is_enabled(self):
        return self.base_is_enabled(page.doctor_activate_new_password_btn)

    # 激活账号③页面-点击设定新密码按钮
    def page_doctor_activate_account_new_password_btn(self):
        self.base_click(page.doctor_activate_new_password_btn)

    # 业务方法——激活账号
    def page_doctor_activate_account_success(self, name, num, phone, code, new_password):
        self.page_doctor_activate_account_btn()
        sleep(1)
        self.page_doctor_activate_account_name_input(name)
        self.page_doctor_activate_account_num_input(num)
        sleep(1)
        self.page_doctor_activate_account_next_step_click()
        self.page_doctor_activate_account_phone_input(phone)
        sleep(1)
        self.page_doctor_activate_account_get_code()
        sleep(3)
        self.page_doctor_activate_account_code_input(code)
        self.page_doctor_activate_account_new_password_input(new_password)
        sleep(1)
        self.page_doctor_activate_account_new_password_btn()
