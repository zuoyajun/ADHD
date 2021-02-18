import os

BASE_PATH = os.path.dirname(__file__)
# print(BASE_PATH)

# 生成html
# allure generate ./report/allure-results -o ./report/allure-html --clean
# 自动打开报告
# allure serve report/allure-results
# 全部运行并生成报告
# pytest  --alluredir ./report/allure-results


# 指定文件运行并生成报告
# pytest --browser=chrome ./scripts/test01_admin_login.py --alluredir ./report/allure-results
# pytest --browser=firefox ./scripts/test01_admin_login.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test02_admin_login_jump.py --alluredir ./report/allure-results
# pytest --browser=firefox ./scripts/test02_admin_login_jump.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test03_admin_login_porget_password.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test04_admin_create_doctor.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test05_admin_doctor_sort.py --alluredir ./report/allure-results

# pytest --browser=chrome  ./scripts/test06_admin_search_doctor.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test07_admin_doctor_detail_change.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test08_admin_doctor_detail_frozen.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test09_admin_account_change_email.py --alluredir ./report/allure-results

# pytest --browser=chrome ./scripts/test10_admin_account_change_password.py --alluredir ./report/allure-results



