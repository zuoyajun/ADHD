
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class GetDriver:
    # 声明变量
    __web_driver = None

    # 获取driver方法

    def get_web_driver(self, url, browser):
        # 判断driver是为空
        if self.__web_driver is None:
            # 获取浏览器
            if browser == 'chrome':
                chrome = Options()
                # 开启静默模式
                # chrome.add_argument("headless")
                chrome.add_argument('--no-sandbox')
                chrome.add_argument('--disable-gpu')

                self.__web_driver = webdriver.Remote(command_executor="http://192.168.1.242:4444/wd/hub",
                                                     desired_capabilities=DesiredCapabilities.CHROME, options=chrome)
            elif browser == 'firefox':
                firefox = Options()
                # firefox.add_argument("headless")
                firefox.add_argument('--no-sandbox')
                firefox.add_argument('--disable-gpu')
                self.__web_driver = webdriver.Remote(command_executor="http://192.168.1.242:4444/wd/hub",
                                                     desired_capabilities=DesiredCapabilities.FIREFOX, options=firefox)

            # 最大化浏览器
            self.__web_driver.maximize_window()
            # 打开url
            self.__web_driver.get(url)
        # 返回driver
        return self.__web_driver

