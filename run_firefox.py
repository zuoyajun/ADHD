import os
os.system("pytest --browser=firefox ./scripts/test01_admin_login.py --alluredir ./report/firefox/allure-results")
# os.system("pytest --browser=firefox --alluredir ./report/firefox/allure-results")
os.system("allure generate ./report/firefox/allure-results -o ./report/firefox/allure-html --clean")
