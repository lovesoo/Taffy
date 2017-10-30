# coding=utf-8

import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from Util import *
from selenium import webdriver
import time

selenium_yml = '/config/selenium.yml'


class test_login(object):
    def __init__(self):
        pass

    @classmethod
    def setUpClass(cls):
        site = ConfigUtil.get('site', path=selenium_yml)
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.url = site['url']
        cls.title = site['title']
        cls.tips = site['tips']
        cls.suffix = site['suffix']
        cls.user = site['user']
        cls.passwd = site['passwd']

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @staticmethod
    def login(self, user, passwd, tips=''):
        # 定义通用login方法
        print 'Login user: %s ,passwd: %s' % (user, passwd)
        # 声明loginPage对象
        login_page = loginPage(self.driver, self.url, self.title)
        # 打开页面
        login_page.open()
        time.sleep(1)
        # 切换到登录框Frame
        login_page.switch_frame('x-URS-iframe')
        time.sleep(1)
        # 输入用户名
        login_page.input_username(user)
        # 输入密码
        login_page.input_password(passwd)
        # 点击登录
        login_page.click_submit()
        time.sleep(1)

        if tips:
            # 登陆失败校验提示信息
            fail_tips = login_page.show_span()
            print 'Login Failed: %s' % fail_tips
            assert tips == fail_tips, 'Check Login Error Tips Failed!'
        else:
            # 登陆成功校验UserID
            login_userID = login_page.show_userid()
            # 点击退出
            login_page.click_logout()
            time.sleep(1)

            print 'Login UserID: %s' % login_userID
            assert user + self.suffix == login_userID, 'Check UserID Failed!'

    def test_BVT(self):
        # 测试用例：用户登陆成功
        test_login.login(self, self.user, self.passwd)

    def test_Err_User(self):
        # 测试用例：用户名错误，登陆失败
        test_login.login(self, 'adcedfg', self.passwd, self.tips)

    def test_Err_Passwd(self):
        # 测试用例：密码错误，登陆失败
        test_login.login(self, self.user, '123456', self.tips)


