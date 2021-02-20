import page
from base.base import Base
from tool.read_json import read_json


class PageAdminLogin(Base):
    # 登录页面-获取系统log
    def page_admin_login_get_log(self):
        # 调用父类中 获取文本方法
        return self.base_get_text(page.admin_login_log)

    # 获取邮箱
    def page_admin_login_get_email(self):
        # 调用父类中 获取文本方法
        return self.base_get_text(page.admin_login_get_email)

    # 输入密码
    def page_admin_login_password(self, password):
        # 调用父类中 输入方法
        self.base_input(page.admin_login_password_input, password)

    # 点击登录按钮
    def page_admin_login_btn(self):
        # 调用父类中 点击方法
        self.base_click(page.admin_login_btn)

    # 获取错误提示信息
    def page_admin_login_get_err(self):
        # 调用父类中 获取文本方法
        return self.base_get_text(page.admin_login_err)

    # 点击医生登录按钮
    def page_admin_login_doctor_btn(self):
        # 调用父类中 点击方法
        self.base_click(page.admin_login_doctor_btn)

    # 点击忘记密码按钮
    def page_admin_login_porget_password(self):
        # 调用父类中 点击方法
        self.base_click(page.admin_login_porget_password_btn)

    # 组合方法--登录
    def page_admin_login(self, password):
        self.page_admin_login_password(password)
        self.page_admin_login_btn()

    # 依赖方法--成功登录
    def page_admin_login_success(self, password=read_json("admin", "page", "login_success.json")['password']):
        self.page_admin_login_password(password)
        self.page_admin_login_btn()
