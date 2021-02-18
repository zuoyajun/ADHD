from page.page_admin_account import PageAdminAccount
from page.page_admin_create_doctor import PageAdminCreateDoctor
from page.page_admin_doctor_detail import PageAdminDoctorDetail
from page.page_admin_doctor_list import PageAdminDoctorList
from page.page_admin_login import PageAdminLogin
from page.page_admin_login_porget_password import PageAdminLoginPorgetPassword
from page.page_doctor_activate_account import PageDoctorActivateAccount
from page.page_doctor_child_list import PageDoctorChildList
from page.page_doctor_login import PageDoctorLogin


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    # 获取 管理员端-登录页面对象
    def page_get_PageAdminLogin(self):
        return PageAdminLogin(self.driver)

    # 获取 管理员端-忘记密码页面对象
    def page_get_PageAdminLoginPorgetPassword(self):
        return PageAdminLoginPorgetPassword(self.driver)

    # 获取 管理员端-创建医生页面对象
    def page_get_PageAdminCreateDoctor(self):
        return PageAdminCreateDoctor(self.driver)

    # 获取 管理员端-医生详情页面对象
    def page_get_PageAdminDoctorDetail(self):
        return PageAdminDoctorDetail(self.driver)

    # 获取 管理员端-医生列表页面对象
    def page_get_PageAdminDoctorList(self):
        return PageAdminDoctorList(self.driver)

    # 获取 管理员端-账户页面对象
    def page_get_PageAdminAccount(self):
        return PageAdminAccount(self.driver)

    # 获取 医生端-登录页面对象
    def page_get_PageDoctorLogin(self):
        return PageDoctorLogin(self.driver)

    # 获取 医生端-激活账号页面对象
    def page_get_PageDoctorActivateAccount(self):
        return PageDoctorActivateAccount(self.driver)

    # 获取 医生端-儿童列表页面对象
    def page_get_PageDoctorChildList(self):
        return PageDoctorChildList(self.driver)
