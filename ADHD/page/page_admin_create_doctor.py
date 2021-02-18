import page
from base.base import Base
from tool.read_json import read_json


class PageAdminCreateDoctor(Base):
    # 点击创建医生按钮
    def page_admin_create_doctor_click(self):
        self.base_click(page.admin_doctor_list_create_btn)

    # 输入医生姓名
    def page_admin_create_doctor_name(self, doctor_name):
        self.base_input(page.admin_create_doctor_name_input, doctor_name)

    # 输入医生身份证号
    def page_admin_create_doctor_num(self, doctor_num):
        self.base_input(page.admin_create_doctor_num_input, doctor_num)

    # 点击创建
    def page_admin_create_doctor_btn(self):
        self.base_click(page.admin_create_doctor_btn)

    # 获取错误提示信息
    def page_admin_create_doctor_get_err(self):
        return self.base_get_text(page.admin_create_doctor_get_err)

    # 关闭创建医生弹窗
    def page_admin_create_doctor_close(self):
        self.base_click(page.admin_create_doctor_close_btn)

    # 组合方法——创建医生
    def page_admin_create_doctor(self, doctor_name, doctor_num):
        self.page_admin_create_doctor_click()
        self.page_admin_create_doctor_name(doctor_name)
        self.page_admin_create_doctor_num(doctor_num)
        self.page_admin_create_doctor_btn()

    # 依赖方法——创建医生-->搜索使用
    def page_admin_create_doctor_success_search(self,
                                                doctor_name=read_json("admin", "page", "create_doctor_success.json")[
                                                    'doctor_name'],
                                                doctor_num=read_json("admin", "page", "create_doctor_success.json")[
                                                    'doctor_num']):
        self.page_admin_create_doctor_click()
        self.page_admin_create_doctor_name(doctor_name)
        self.page_admin_create_doctor_num(doctor_num)
        self.page_admin_create_doctor_btn()
