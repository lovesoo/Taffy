# coding=utf-8

"""
loginPageUtil.py
页面基本操作方法，如open，input_username，input_password，click_submit
"""

from selenium.webdriver.common.by import By
from .basePageUtil import basePage
from Util import *
selenium_yml = '/config/selenium.yml'


class loginPage(basePage):
    # 继承basePage类
    loc = ConfigUtil.get('loc', path=selenium_yml)

    # 定位器，通过元素属性定位元素对象
    username_loc = eval(loc['username_loc'])
    password_loc = eval(loc['password_loc'])
    submit_loc = eval(loc['submit_loc'])
    span_loc = eval(loc['span_loc'])
    dynpw_loc = eval(loc['dynpw_loc'])
    userid_loc = eval(loc['userid_loc'])
    logout_loc = eval(loc['logout_loc'])
    # 操作
    # 通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    # 打开网页

    def open(self):
        # 调用page中的_open打开连接
        self._open(self.url, self.pagetitle)
    # 输入用户名：调用send_keys对象，输入用户名

    def input_username(self, username):
        self.send_keys(self.username_loc, username, clear_first=True)
    # 输入密码：调用send_keys对象，输入密码

    def input_password(self, password):
        self.send_keys(self.password_loc, password, clear_first=True)
    # 点击登录：调用send_keys对象，点击登录

    def click_submit(self):
        self.find_element(self.submit_loc).click()
    # 用户名或密码不合理是Tip框内容展示

    def show_span(self):
        try:
            tips = self.find_element(self.span_loc)
            if tips:
                return tips.text
            else:
                return None
        except Exception as e:
            print(e)
    # 切换登录模式为动态密码登录（IE下有效）

    def swich_DynPw(self):
        self.find_element(self.dynpw_loc).click()
    # 登录成功页面中的用户ID查找

    def show_userid(self):
        return self.find_element(self.userid_loc).text
    # 登陆退出：调用send_keys对象，点击退出

    def click_logout(self):
        self.find_element(self.logout_loc).click()
