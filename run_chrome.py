import os
os.system("pytest --browser=chrome ./scripts/test01_admin_login.py --alluredir ./report/allure-results")
# os.system("pytest --browser=chrome --alluredir ./report/allure-results")
os.system("allure generate ./report/allure-results -o ./report/allure-html --clean")
