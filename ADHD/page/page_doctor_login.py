import page
from base.base import Base
from tool.read_json import read_json


class PageDoctorLogin(Base):
    # 获取登录页面-系统log
    def page_doctor_login_get_log(self):
        return self.base_get_text(page.doctor_login_log)

    # 输入手机号
    def page_doctor_login_phone_input(self, phone):
        self.base_input(page.doctor_login_phone_input, phone)

    # 输入密码
    def page_doctor_login_password_input(self, password):
        self.base_input(page.doctor_login_password_input, password)

    # 点击登录按钮
    def page_doctor_login_btn(self):
        self.base_click(page.doctor_login_btn)

    # 获取错误提示信息
    def page_doctor_login_get_err(self):
        return self.base_get_text(page.doctor_login_err)

    # 点击忘记密码按钮
    def page_doctor_login_porget_password_btn(self):
        self.base_click(page.doctor_login_porget_password_btn)

    # 点击管理员登录按钮
    def page_doctor_login_admin_btn(self):
        # 调用父类中 点击方法
        self.base_click(page.doctor_login_admin_btn)

    # 组合方法--登录
    def page_doctor_login(self, phone, password):
        self.page_doctor_login_phone_input(phone)
        self.page_doctor_login_password_input(password)
        self.page_doctor_login_btn()

    # 组合方法-成功登录
    def page_doctor_login_success(self,
                                  phone=read_json("doctor", "page", "login_success.json")['phone'],
                                  password=read_json("doctor", "page", "login_success.json")['password']):
        self.page_doctor_login_phone_input(phone)
        self.page_doctor_login_password_input(password)
        self.page_doctor_login_btn()

