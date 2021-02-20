from time import sleep
import allure
import pytest
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.get_logger import GetLogger
from tool.get_mysql import get_select_mysql
from tool.read_yaml import read_yaml

log = GetLogger.get_logger()


@pytest.fixture(autouse=True, scope="class")
def premise(browser):
    # 1.获取driver
    admin_driver = GetDriver().get_web_driver(page.admin_url, browser)
    # 2.调用 成功登录依赖方法
    PageIn(admin_driver).page_get_PageAdminLogin().page_admin_login_success()
    # 3.获取 医生列表页面对象
    admin_doctor_list = PageIn(admin_driver).page_get_PageAdminDoctorList()
    yield admin_doctor_list

    admin_driver.quit()


# 跳过用例
# @pytest.mark.skipif(reason="暂不使用")
class TestAdminDoctorSort:
    @allure.epic("管理员端")
    @allure.feature("医生列表排序用例")
    @allure.title("{titles}")
    @allure.severity("minor")
    @allure.description("""
    用例描述：
        1.调用登录方法
        2.姓名拼写+升序排序，对医生列表前3个医生姓名进行校验
        3.姓名拼写+降序排序，对医生列表前3个医生姓名进行校验
        4.创建日期+升序排序，对医生列表前3个医生姓名进行校验
        5.创建日期+降序排序，对医生列表前3个医生姓名进行校验

    参数描述：
        1.sort: 排序方式
        2.mysql：查询语句
        3.titles：用例标题
            """)
    # 业务方法--排序
    @pytest.mark.parametrize("sort,mysql,titles", read_yaml("admin", "scripts", "doctor_sort.yaml"))
    def test_admin_doctor_sort(self, sort, mysql, titles, premise):
        admin_doctor_list = premise
        if sort == "name+asc":
            with allure.step("调用姓名+升序方法"):
                admin_doctor_list.page_admin_doctor_list_name_asc()

        if sort == "name+desc":
            with allure.step("调用姓名+降序方法"):
                admin_doctor_list.page_admin_doctor_list_name_desc()

        if sort == "data+asc":
            with allure.step("调用日期+升序方法"):
                admin_doctor_list.page_admin_doctor_list_data_asc()

        if sort == "data+desc":
            with allure.step("调用日期+降序方法"):
                admin_doctor_list.page_admin_doctor_list_data_desc()

        with allure.step("调用查询数据库方法"):
            doctor_sort = get_select_mysql(mysql)
        sleep(2)

        with allure.step("断言医生列表前3个医生的姓名"):
            try:
                assert admin_doctor_list.page_admin_doctor_list_get_first_doctor_name() == doctor_sort[0][0]
                assert admin_doctor_list.page_admin_doctor_list_get_second_doctor_name() == doctor_sort[1][0]
                assert admin_doctor_list.page_admin_doctor_list_get_third_doctor_name() == doctor_sort[2][0]
            except AssertionError as e:
                log.error("排序断言出错，错误信息：{}".format(e))
                admin_doctor_list.base_get_image()
                raise e
