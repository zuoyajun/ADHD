import os
import time
import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_PATH
from tool.get_logger import GetLogger

log = GetLogger.get_logger()


class Base:

    # 初始化
    def __init__(self, driver):
        self.driver = driver
        log.info("正在获取driver：{}".format(driver))

    # 1.查找 方法封装
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        """
        使用显示等待 查找元素
        :param loc: 元素的定位信息，格式为元祖
        :param timeout: 默认超时时间为30秒
        :param poll: 访问频率，默认0.5秒查找一次
        :return: 返回查找到的元素
        """
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 2.点击 方法封装
    def base_click(self, loc):
        # 获取元素并点击
        self.base_find_element(loc).click()
        log.info("正在对：{}元素执行点击操作！".format(loc))

    # 3.输入 方法封装(clear方式清空)
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空
        log.info("正在对：{}元素执行清空操作！".format(loc))
        el.clear()
        # 输入
        log.info("正在对：{}元素执行输入：{}".format(loc, value))
        el.send_keys(value)

    # 4.输入 方法封装(全选+delete方式清空)
    def base_send_input(self, loc, value):
        # 获取元素
        el = self.base_find_element(loc)
        # 清空
        log.info("正在对：{}元素执行清空操作！".format(loc))
        el.click()
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.DELETE)
        # 输入
        log.info("正在对：{}元素执行输入：{}".format(loc, value))
        el.send_keys(value)

    # 5.获取文本信息text 方法封装
    def base_get_text(self, loc):
        get_text = self.base_find_element(loc).text
        log.info("正在对：{}元素获取文本操作！获取的文本值：{}".format(loc, get_text))
        return get_text

    # 6.判断元素是否可用
    def base_is_enabled(self, loc):
        is_enabled = self.base_find_element(loc).is_enabled()
        log.info("正在对：{}元素判断是否可用，返回值为：{}".format(loc, is_enabled))
        return is_enabled

    # 7.浏览器后退按钮
    def base_driver_back(self):
        self.driver.back()
        log.info("正在点击浏览器后退按钮！")

    # 8.截图+失败截图写入allure报告 方法封装
    def base_get_image(self):
        log.info("断言出错，正在执行截图操作！")
        image_path = BASE_PATH + os.sep + 'image' + os.sep + "{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S"))
        self.driver.get_screenshot_as_file(image_path)
        # 获取图片写入文件流
        with open(image_path, mode='rb') as f:
            file = f.read()
        allure.attach(file, "失败截图", allure.attachment_type.PNG)
        log.info("断言出错，正在将错误图片写入allure报告！")
