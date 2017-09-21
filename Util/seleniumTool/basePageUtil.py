# coding=utf-8

"""
basePageUtil.py
基础类basePage，封装所有页面都公用的方法，
定义open函数，重定义find_element,switch_frame,send_keys等函数。
在初始化方法中定义驱动driver,url,pagetitle
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basePage(object):
    """
    basePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """
    # 初始化driver,url,pagetitle等
    # 实例化basePage类时，最先执行的就是__init__方法，该方法的入参，其实就是basePage类的入参。
    #__init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。

    def __init__(self, selenium_driver, url, pagetitle):
        self.driver = selenium_driver
        self.url = url
        self.pagetitle = pagetitle

    # 通过title断言进入的页面是否正确。
    # 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True 或 False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    # 打开页面，并校验页面链接是否加载正确
    # 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的。
    def _open(self, url, pagetitle):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page()方法
        assert self.on_page(pagetitle), "Open Page Error:\t%s" % url

    # 定义open方法，调用_open()进行打开链接
    def open(self):
        self._open(self.url, self.pagetitle)

    # 重写元素定位方法
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except BaseException:
            print '%s page does not have "%s" locator' % (self, loc)

    # 重写switch_frame方法
    def switch_frame(self, loc):
        return self.driver.switch_to_frame(loc)

    # 定义script方法，用于执行js脚本
    def script(self, src):
        self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            # getattr相当于实现self.loc
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()

            self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print '%s page does not have "%s" locator' % (self, loc)
