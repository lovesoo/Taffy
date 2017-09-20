# coding=utf-8
from checkUtil import *
import re

class check_response():
    @staticmethod
    def check_title(response,key):
        #校验key是否匹配返回页面title
        expect_title=key+u'_百度搜索'
        re_title=re.compile('<title>(.*)</title>')  #搜索页面title正则表达式
        title=re.search(re_title,response).groups()[0]
        print 'Search Result Title:%s'%title
        eq_(title,expect_title,'Title Check Error!%s != %s'%(title,expect_title))

    @staticmethod
    def check_results(response,key):
        #校验key是否匹配搜索结果的名称或者URL
        re_name=re.compile('>(.*)</a></h3>')    #搜索结果name正则表达式
        re_url=re.compile('style="text-decoration:none;">(.*)</a><div') #搜索结果url正则表达式
        names=re.findall(re_name,response)
        urls=re.findall(re_url,response)

        for name,url in zip(names,urls):
            #name,url简单处理，去除特殊符号
            name=name.replace('</em>','').replace('<em>','')
            url = url.replace('<b>', '').replace('</b>', '').replace('&nbsp;', '').replace('...', '')
            print 'Search Results Name:%s\tURL:%s'%(name,url)
            if key.lower() not in (name+url).lower():
                assert False,'Search Results Check Error!%s not in %s'%(key,name+url)
        return True
