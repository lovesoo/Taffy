# encoding: utf-8

import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
import json
from datetime import datetime as dt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from functools import partial
from nose.tools import *


def send_mail():
    # 读取测试报告内容
    with open(report_file, 'r') as f:
        content = f.read().decode('utf-8')

    msg = MIMEMultipart('mixed')
    # 添加邮件内容
    msg_html = MIMEText(content, 'html', 'utf-8')
    msg.attach(msg_html)

    # 添加附件
    msg_attachment = MIMEText(content, 'html', 'utf-8')
    msg_attachment["Content-Disposition"] = 'attachment; filename="{0}"'.format(report_file)
    msg.attach(msg_attachment)

    msg['Subject'] = mail_subjet
    msg['From'] = mail_user
    msg['To'] = ';'.join(mail_to)
    try:
        # 连接邮件服务器
        s = smtplib.SMTP(mail_host, 25)
        # 登陆
        s.login(mail_user, mail_pwd)
        # 发送邮件
        s.sendmail(mail_user, mail_to, msg.as_string())
        # 退出
        s.quit()
    except Exception as e:
        print "Exceptioin ", e


class check_response():
    @staticmethod
    def check_result(response, params, expectNum=None):
        # 由于搜索结果存在模糊匹配的情况，这里简单处理只校验第一个返回结果的正确性
        if expectNum is not None:
            # 期望结果数目不为None时，只判断返回结果数目
            eq_(expectNum, len(response['subjects']), '{0}!={1}'.format(expectNum, len(response['subjects'])))
        else:
            if not response['subjects']:
                # 结果为空，直接返回失败
                assert False
            else:
                # 结果不为空，校验第一个结果
                subject = response['subjects'][0]
                # 先校验搜索条件tag
                if params.get('tag'):
                    for word in params['tag'].split(','):
                        genres = subject['genres']
                        ok_(word in genres, 'Check {0} failed!'.format(word.encode('utf-8')))

                # 再校验搜索条件q
                elif params.get('q'):
                    # 依次判断片名，导演或演员中是否含有搜索词，任意一个含有则返回成功
                    for word in params['q'].split(','):
                        title = [subject['title']]
                        casts = [i['name'] for i in subject['casts']]
                        directors = [i['name'] for i in subject['directors']]
                        total = title + casts + directors
                        ok_(any(word.lower() in i.lower() for i in total),
                            'Check {0} failed!'.format(word.encode('utf-8')))

    @staticmethod
    def check_pageSize(response):
        # 判断分页结果数目是否正确
        count = response.get('count')
        start = response.get('start')
        total = response.get('total')
        diff = total - start

        if diff >= count:
            expectPageSize = count
        elif count > diff > 0:
            expectPageSize = diff
        else:
            expectPageSize = 0

        eq_(expectPageSize, len(response['subjects']), '{0}!={1}'.format(expectPageSize, len(response['subjects'])))


class test_doubanSearch(object):
    """接口名称"""

    @staticmethod
    def search(params, expectNum=None):
        url = 'https://api.douban.com/v2/movie/search'
        r = requests.get(url, params=params)
        print 'Search Params:\n', json.dumps(params, ensure_ascii=False)
        print 'Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4)
        code = r.json().get('code')
        if code > 0:
            assert False, 'Invoke Error.Code:\t{0}'.format(code)
        else:
            if params.get('start') is not None or params.get('count') is not None:
                # 传入start参数时，只校验翻页功能
                check_response.check_pageSize(r.json())
            else:
                # 校验搜索结果是否与搜索词匹配
                check_response.check_result(r.json(), params, expectNum)

    def test_q(self):
        # 校验搜索条件 q
        qs = [u'白夜追凶', u'大话西游', u'周星驰', u'张艺谋', u'周星驰,吴孟达', u'张艺谋,巩俐', u'周星驰,大话西游', u'白夜追凶,潘粤明']
        for q in qs:
            params = dict(q=q)
            f = partial(test_doubanSearch.search, params)
            f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)

    def test_tag(self):
        # 校验搜索条件 tag
        tags = [u'科幻', u'喜剧', u'动作', u'犯罪', u'科幻,喜剧', u'动作,犯罪']
        for tag in tags:
            params = dict(tag=tag)
            f = partial(test_doubanSearch.search, params)
            f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)

    def test_param_combination(self):
        # 校验组合搜索q,tag
        params_list = [(dict(q='', tag=''), 0),
                       dict(q=u'刘德华', tag=''),
                       dict(q='', tag=u'动作'),
                       dict(q=u'刘德华', tag=u'动作')]
        for params in params_list:
            if isinstance(params, tuple):
                f = partial(test_doubanSearch.search, params[0], params[1])
                f.description = json.dumps(params[0], ensure_ascii=False).encode('utf-8')
            else:
                f = partial(test_doubanSearch.search, params)
                f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)

    def test_page(self):
        # 校验接口翻页返回结果功能是否正常
        q = u'周星驰'
        count = 15
        for page in range(10):
            start = page * count
            params = dict(q=q, start=start, count=count)
            f = partial(test_doubanSearch.search, params)
            f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)

    def test_param_q(self):
        # 参数校验 q，搜索类型：中文、英文、数字、特殊符号、None、空
        qs = [u'战狼', (u'avatar', 20), u'2046', (u'~!@#$%^&*()', 0), (None, 0), ('', 0)]
        for q in qs:
            if isinstance(q, tuple):
                params = dict(q=q[0])
                f = partial(test_doubanSearch.search, params, q[1])
                f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            else:
                params = dict(q=q)
                f = partial(test_doubanSearch.search, params)
                f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)

    def test_param_tag(self):
        # 参数校验 tag，搜索类型：中文、英文、数字、特殊符号、None、空
        tags = [u'喜剧', (u'action', 20), (u'2046', 20), (u'~!@#$%^&*()', 0), (None, 0), ('', 0)]
        for tag in tags:
            if isinstance(tag, tuple):
                params = dict(tag=tag[0])
                f = partial(test_doubanSearch.search, params, tag[1])
                f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            else:
                params = dict(tag=tag)
                f = partial(test_doubanSearch.search, params)
                f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)

    def test_param_start(self):
        q = u'周星驰'
        start_list = [None, 0, 10, 100, -1]
        for start in start_list:
            params = dict(q=q, start=start)
            f = partial(test_doubanSearch.search, params)
            f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)

    def test_param_count(self):
        tag = u'喜剧'
        count_list = [None, 20, 10, 100, 0, -10]
        for count in count_list:
            params = dict(tag=tag, count=count)
            f = partial(test_doubanSearch.search, params)
            f.description = json.dumps(params, ensure_ascii=False).encode('utf-8')
            yield (f,)


if __name__ == '__main__':
    # 邮件服务器
    mail_host = 'smtp.163.com'
    # 发件人地址
    mail_user = 'xxx@163.com'
    # 发件人密码
    mail_pwd = 'xxx'
    # 邮件标题
    mail_subjet = u'NoseTests_测试报告_{0}'.format(dt.now().strftime('%Y%m%d'))
    # 收件人地址list
    mail_to = ['xxx@126.com', 'xxx@126.com']
    # 测试报告名称
    report_file = 'TestReport.html'

    # 运行nosetests进行自动化测试并生成测试报告
    print 'Run Nosetests Now...'
    os.system('nosetests -v test_doubanSearch.py:test_doubanSearch --with-html --html-file={0}'.format(report_file))

    # 发送测试报告邮件
    print 'Send Test Report Mail Now...'
    send_mail()
