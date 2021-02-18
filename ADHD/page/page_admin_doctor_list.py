from time import sleep
import page
from base.base import Base
from tool.get_logger import GetLogger

log = GetLogger.get_logger()


class PageAdminDoctorList(Base):
    # 获取系统log
    def page_admin_doctor_list_get_log(self):
        return self.base_get_text(page.admin_doctor_list_log)

    # 点击医生列表按钮
    def page_admin_doctor_list_btn(self):
        self.base_click(page.admin_doctor_list_btn)

    # 点击账户按钮
    def page_admin_doctor_list_account(self):
        self.base_click(page.admin_doctor_list_account_btn)

    # 输入医生姓名
    def page_admin_doctor_list_search_name(self, search_name):
        self.base_input(page.admin_doctor_list_search_input, search_name)

    # 点击搜索按钮
    def page_admin_doctor_list_search_btn(self):
        self.base_click(page.admin_doctor_list_search_btn)

    # 点击排序方式第一个下拉框
    def page_admin_doctor_list_sort_one(self):
        self.base_click(page.admin_doctor_list_sort_one)

    # 点击排序方式第二个下拉框
    def page_admin_doctor_list_sort_two(self):
        self.base_click(page.admin_doctor_list_sort_two)

    # 排序方式
    def page_admin_doctor_list_sort(self, sort_loc1, sort_loc2):
        self.page_admin_doctor_list_sort_one()
        sleep(1)
        self.base_click(sort_loc1)
        sleep(1)
        self.page_admin_doctor_list_sort_two()
        sleep(1)
        self.base_click(sort_loc2)
        sleep(1)

    # 排序方式：按创建日期+升序
    def page_admin_doctor_list_data_asc(self):
        self.page_admin_doctor_list_sort(page.admin_doctor_list_sort_data, page.admin_doctor_list_sort_asc)

    # 排序方式：按创建日期+降序
    def page_admin_doctor_list_data_desc(self):
        self.page_admin_doctor_list_sort(page.admin_doctor_list_sort_data, page.admin_doctor_list_sort_desc)

    # 排序方式：按姓名拼写+升序
    def page_admin_doctor_list_name_asc(self):
        self.page_admin_doctor_list_sort(page.admin_doctor_list_sort_name, page.admin_doctor_list_sort_asc)

    # 排序方式：按姓名拼写+降序
    def page_admin_doctor_list_name_desc(self):
        self.page_admin_doctor_list_sort(page.admin_doctor_list_sort_name, page.admin_doctor_list_sort_desc)

    # 点击医生列表第一个医生的详情按钮
    def page_admin_doctor_list_click_first_doctor_detail(self):
        self.base_click(page.admin_doctor_list_first_detail)

    # 获取医生列表第一个医生的姓名
    def page_admin_doctor_list_get_first_doctor_name(self):
        return self.base_get_text(page.admin_doctor_list_first_name)

    # 获取医生列表第二个医生的姓名
    def page_admin_doctor_list_get_second_doctor_name(self):
        return self.base_get_text(page.admin_doctor_list_second_name)

    # 获取医生列表第三个医生的姓名
    def page_admin_doctor_list_get_third_doctor_name(self):
        return self.base_get_text(page.admin_doctor_list_third_name)

    # 组合方法--搜索医生
    def page_admin_doctor_list_search(self, search_name):
        self.page_admin_doctor_list_search_name(search_name)
        self.page_admin_doctor_list_search_btn()
