import os
os.system("pytest --browser=chrome ./scripts/test01_admin_login.py --alluredir ./report/chrome/allure-results")
# os.system("pytest --browser=chrome --alluredir ./report/chrome/allure-results")
os.system("allure generate ./report/chrome/allure-results -o ./report/chrome/allure-html --clean")
