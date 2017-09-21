# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append('../..')
from Util import *
from selenium import webdriver
import time


class test_login(object):
    def __init__(self):
        pass

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.url = "http://mail.126.com"
        self.suffix = '@126.com'
        self.user = "tafffy"
        self.passwd = "lovesoo1314"
        self.title = u'网易'
        self.tips = u'帐号或密码错误'

    def tearDown(self):
        self.driver.quit()

    @staticmethod
    @with_setup(setUp, tearDown)
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

        # 检查是否登陆失败
        fail_tips = login_page.show_span()
        if fail_tips:
            print 'Login Failed: %s' % fail_tips
            if tips:
                # 登陆失败提示信息校验
                assert tips == fail_tips, 'Check Login Error Tips Failed!%s'
        else:
            # 登陆成功用户名校验
            login_userID = login_page.show_userid()
            print 'Login Success.UserID: %s' % login_userID
            assert user + self.suffix == login_userID, 'Check Login UserID Failed!'

    def test_BVT(self):
        # 测试用例：用户登陆成功
        test_login.login(self, self.user, self.passwd)

    def test_Err_User(self):
        # 测试用例：用户名错误，登陆失败
        test_login.login(self, 'adcedfg', self.passwd, self.tips)

    def test_Err_Passwd(self):
        # 测试用例：密码错误，登陆失败
        test_login.login(self, self.user, '123456', self.tips)
