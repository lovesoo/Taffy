# encoding: utf-8

import requests
import re
from nose.tools import *


class check_response():
    @staticmethod
    def check_title(response, key):
        # 校验key是否匹配返回页面title
        expect_title = key + u'_百度搜索'
        re_title = re.compile('<title>(.*)</title>')  # 搜索页面title正则表达式
        title = re.search(re_title, response).groups()[0]
        print 'Search Result Title:%s' % title
        eq_(title, expect_title, 'Title Check Error!%s != %s' % (title, expect_title))

    @staticmethod
    def check_results(response, key):
        # 校验key是否匹配搜索结果的名称或者URL
        re_name = re.compile('>(.*)</a></h3>')  # 搜索结果name正则表达式
        re_url = re.compile('style="text-decoration:none;">(.*)</a><div')  # 搜索结果url正则表达式
        names = re.findall(re_name, response)
        urls = re.findall(re_url, response)

        for name, url in zip(names, urls):
            # name,url简单处理，去除特殊符号
            name = name.replace('</em>', '').replace('<em>', '')
            url = url.replace('<b>', '').replace('</b>', '').replace('&nbsp;', '').replace('...', '')
            print 'Search Results Name:%s\tURL:%s' % (name, url)
            if key.lower() not in (name + url).lower():
                assert False, 'Search Results Check Error!%s not in %s' % (key, name + url)
        return True


class test_baiduSearch(object):
    """接口名称"""

    def __init__(self, ):
        """Constructor for test_baiduSearch"""

    @staticmethod
    def search(wd):
        url = 'http://www.baidu.com/s'
        params = dict(wd=wd)
        r = requests.get(url, params=params)

        # 检查百度搜索返回页面标题
        check_response.check_title(r.text, wd)
        # 检查百度页面返回内容
        check_response.check_results(r.text, wd)

    def test_BVT(self):
        # 校验输入不同类型的wd时，百度是否均可正常搜索返回结果
        # wd分类：中文，英文，数字
        wd_list = [u'lovesoo', u'软件测试', u'12345']
        for wd in wd_list:
            yield test_baiduSearch.search, wd
