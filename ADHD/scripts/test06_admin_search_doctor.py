from time import sleep
import allure
import page
import pytest
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_logger import GetLogger
from tool.get_mysql import get_mysql
from tool.read_yaml import read_yaml

log = GetLogger.get_logger()


@pytest.fixture(autouse=True, scope="class")
def premise(browser):
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 调用 成功登录依赖方法
    PageIn(admin_driver).page_get_PageAdminLogin().page_admin_login_success()
    # 调用 成功创建医生依赖方法
    PageIn(admin_driver).page_get_PageAdminCreateDoctor().page_admin_create_doctor_success_search()
    # 获取 医生列表页面对象
    admin_doctor_list = PageIn(admin_driver).page_get_PageAdminDoctorList()
    yield admin_doctor_list

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminSearchDoctor:
    @allure.epic("管理员端")
    @allure.feature("搜索医生用例")
    @allure.title('{titles}')
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.调用登录方法
        2.调用创建医生方法
        3.调用搜索医生的方法
        4.对医生列表第一个医生的姓名进行校验
        5.删除创建的医生

    参数描述：
        1.doctor_name：搜索的医生姓名
        2.expect：期望结果
        3.doctor_create_delete_relevance：删除关联sql
        4.doctor_create_delete：删除数据sql
        5.titles：用例标题
                """)
    # 搜索医生--业务方法
    @pytest.mark.parametrize("doctor_name,expect,doctor_create_delete_relevance,doctor_create_delete,titles",
                             read_yaml("admin", "scripts", "search_doctor.yaml"))
    def test_admin_search_doctor(self,
                                 doctor_name,
                                 expect,
                                 doctor_create_delete_relevance,
                                 doctor_create_delete,
                                 titles,
                                 premise):
        admin_doctor_list = premise

        sleep(3)
        with allure.step("调用搜索医生方法"):
            admin_doctor_list.page_admin_doctor_list_search(doctor_name)
        sleep(2)
        with allure.step("断言搜索结果"):
            try:
                assert expect in admin_doctor_list.page_admin_doctor_list_get_first_doctor_name()
            except AssertionError as e:
                log.error("搜索断言出错，错误信息：{}".format(e))
                admin_doctor_list.base_get_image()
                raise e
        with allure.step("删除创建的数据"):
            get_mysql(doctor_create_delete_relevance)
            log.info("删除关联")
            get_mysql(doctor_create_delete)
            log.info("删除创建的数据")
