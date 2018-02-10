# coding=utf-8

import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Util import *
from functools import partial


class test_demo(object):
    """接口测试demo"""

    def __init__(self, ):
        pass

    @staticmethod
    def baidu(wd):
        name = 's'
        sreq = HttpParam(wd=wd)
        sres = BaiduHttpUtil.get(name, sreq)

        # 检查百度搜索返回页面标题
        resultCheck_baidu.check_title(sres, wd)
        # 检查百度页面返回内容
        resultCheck_baidu.check_results(sres, wd)

    def test_http(self):
        # http接口调用demo
        # 校验输入不同类型的wd时，百度是否均可正常搜索返回结果
        # wd分类：中文，英文，数字
        wd_list = [u'taffy', u'自动化测试', u'12345']
        for wd in wd_list:
            f = partial(test_demo.baidu, wd)
            f.description = 'search: %s' % wd
            yield (f,)

    def test_httpbin_get(self):
        # httpbin.org接口测试demo
        # get请求
        name = 'get'
        sreq = HttpbinParam(name='Taffy', description='Taffy is a Test Automation Framework based on nosetests')
        sres = HttpbinUtil.get(name, sreq)
        resultCheck_httpbin.check_get(sres, sreq)

    def test_httpbin_post(self):
        # httpbin.org接口测试demo
        # post请求
        name = 'post'
        sreq = HttpbinParam(name='Taffy', description='Taffy is a Test Automation Framework based on nosetests')
        sres = HttpbinUtil.post(name, sreq)
        resultCheck_httpbin.check_post(sres, sreq)

    @nottest
    def test_hessian(self):
        # hessian接口调用demo
        method = 'delete'
        req = protocol.object_factory('com.service.dubbo.base.req.BaseRequest')
        id = 123456789
        HessianUtil.Invoke(method, req, id)

    @nottest
    def test_webservice(self):
        # webservice接口调用demo
        url = 'http://www.gpsso.com/WebService/Dream/Dream.asmx?wsdl'
        WebServiceUtil.Invoke(url, "SearchDreamInfo", u'太阳')

    @nottest
    def test_db(self):
        # 数据库操作demo
        print DBUtil.execute('select * from user_info;')
        print DBUtil.execute('select * from user_info;', confSection='Sqlserver')

    @nottest
    def test_OA(self):
        # 正交表设计测试用例demo
        oat = OAT()
        case1 = OrderedDict([('K1', [0, 1]),
                             ('K2', [0, 1]),
                             ('K3', [0, 1])])

        case2 = OrderedDict([('A', ['A1', 'A2', 'A3']),
                             ('B', ['B1', 'B2', 'B3', 'B4']),
                             ('C', ['C1', 'C2', 'C3']),
                             ('D', ['D1', 'D2'])])

        case3 = OrderedDict([(u'对比度', [u'正常', u'极低', u'低', u'高', u'极高']),
                             (u'色彩效果', [u'无', u'黑白', u'棕褐色', u'负片', u'水绿色']),
                             (u'感光度', [u'自动', 100, 200, 400, 800]),
                             (u'白平衡', [u'自动', u'白炽光', u'日光', u'荧光', u'阴光']),
                             (u'照片大小', ['5M', '3M', '2M', '1M', 'VGA']),
                             (u'闪光模式', [u'开', u'关'])])

        case4 = OrderedDict([('A', ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']),
                             ('B', ['B1']),
                             ('C', ['C1'])])

        print json.dumps(oat.genSets(case1))
        print json.dumps(oat.genSets(case2))
        print json.dumps(oat.genSets(case3))
        print json.dumps(oat.genSets(case4))
        print json.dumps(oat.genSets(case4, 1, 0))
        print json.dumps(oat.genSets(case4, 1, 1))
        print json.dumps(oat.genSets(case4, 1, 2))
        print json.dumps(oat.genSets(case4, 1, 3))

    @nottest
    def test_redis(self):
        # redis/redis cluster操作 demo
        print RedisUtil.execute('hexists', 'Search:HotWord', u'刘德华')
        print RedisUtil.execute("get", "userSession:%s", "12345", confSection='Redis_Cluster')

    @nottest
    def test_security(self):
        # 加密方法使用demo
        import string
        sec = Security()
        key_8 = string.lowercase[:8]
        key_16 = string.lowercase[:16]
        data = 'Taffy is a Test Automation Framework based on nosetests.'

        print 'DES:', sec.getDES(key_8, data).encode('hex')  # des
        print 'Decode DES:', sec.decodeDES(key_8, sec.getDES(key_8, data))  # decode des
        print 'DES3:', sec.getDES3(key_16, data).encode('hex')  # desc3
        print 'Decode DES3:', sec.decodeDES3(key_16, sec.getDES3(key_16, data))  # decode desc3
        print 'HMAC_SHA1:', sec.getHMAC_SHA1(key_8, data)  # sha1
        print 'SHA:', sec.getSHA(data)  # sha
        print 'MD5:', sec.getMD5(data)  # md5
        print 'AES:', sec.getAES(key_16, data).encode('hex')  # aes
        print'Base64:', sec.getBase64(data)  # base64
        print'Decode Base64:', sec.decodeBase64(sec.getBase64(data))  # decode base64
