import smtplib
import json
from email.mime.text import MIMEText
from email.header import Header
import time
from tool.get_logger import GetLogger
from datetime import date

log = GetLogger.get_logger()
date = date.today()


def send_mail(body):
    try:
        # 邮件正文是MIMEText
        msg = MIMEText(body, 'html', 'utf-8')
        # 邮件对象
        msg['Subject'] = Header("ADHD项目-WEB自动化-测试报告{}".format(date), 'utf-8').encode()  # 标题
        msg['From'] = Header(u'{} <{}>'.format('zuoyajun@66nao.com', sender))  # 来自
        msg['To'] = Header(u'收件人 <%s>' % recipient)  # 发送的用户
        msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")  # 发送时间日期
        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com', 25)  # 邮箱服务器，需查看服务器是否开启25端口
        smtp.login(username, password)  # 登录邮箱
        smtp.sendmail(sender, recipient.split(','), msg.as_string())  # 发送者和接收者
        smtp.quit()
        log.info("邮件已发出，注意查收！")
    except Exception as e:
        log.error("邮件发送失败！".format(e))


def get_chrome_result():
    with open("./report/chrome/allure-html/widgets/summary.json", 'r') as load_f:
        load_dict = json.load(load_f)
        return load_dict


def get_firefox_result():
    with open("./report/chrome/allure-html/widgets/summary.json", 'r') as load_f:
        load_dict = json.load(load_f)
        return load_dict


# 发件箱用户名
username = 'zuoyajun@66nao.com'
# 发件箱密码
password = "Zcx19960127"
# 发件人邮箱
sender = 'zuoyajun@66nao.com'
# 收件人邮箱
recipient = 'zuoyajun@66nao.com'
# weimingyue@66nao.com,shenzhi@66nao.com,
chrome = 'http://192.168.1.246:8080/report/chrome{}/allure-html/index.html'.format(date)
firefox = 'http://192.168.1.246:8080/report/firefox{}/allure-html/index.html'.format(date)

chrome_result = get_chrome_result()
firefox_result = get_firefox_result()

body = """
        <h4>浏览器覆盖范围：</h4>
        <p>Chrome  88.0.4324.190(64位)、Firefox 83.0(64位)</p>
        <h4>Chrome执行用例情况：</h4>
        <p>总共执行用例{}条：通过{}条，失败{}条，跳过{}条，故障{}条，未知{}条</p>
        <h4>Firefox执行用例情况：</h4>
        <p>总共执行用例{}条：通过{}条，失败{}条，跳过{}条，故障{}条，未知{}条</p>
        <h4>报告地址：</h4>
        <p><a href={}>{}</a></p>
        <p><a href={}>{}</a></p>
        """.format(chrome_result['statistic']['total'],
                   chrome_result['statistic']['passed'],
                   chrome_result['statistic']['failed'],
                   chrome_result['statistic']['skipped'],
                   chrome_result['statistic']['broken'],
                   chrome_result['statistic']['unknown'],
                   firefox_result['statistic']['total'],
                   firefox_result['statistic']['passed'],
                   firefox_result['statistic']['failed'],
                   firefox_result['statistic']['skipped'],
                   firefox_result['statistic']['broken'],
                   firefox_result['statistic']['unknown'],
                   chrome,
                   chrome,
                   firefox,
                   firefox)
send_mail(body)
