# coding=utf-8

import suds
import json
from logging import getLogger
log = getLogger('suds')
log.setLevel(30)


class WebServiceUtil(object):
    """webservices调用封装类"""

    def __init__(self):
        pass

    @classmethod
    def Invoke(cls, url, method, *args):
        """接口方法，返回结果
        :param url: webservice访问地址
        :type url: string
        :param method: 方法名
        :type method: string
        :param args: 传入调用接口使用的参数
        :type args: 随便传，列表形式的
        """
        try:
            print 'Request: \t', [json.dumps(i, ensure_ascii=False, indent=4) for i in args]
            client = suds.client.Client(url)
            response = getattr(client.service, method)(*args)
            print 'Response: \t', response
            return response
        except Exception as e:
            print e
