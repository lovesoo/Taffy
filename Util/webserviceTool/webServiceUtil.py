# coding=utf-8
from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor


class WebServiceUtil(object):
    """webservices调用封装类"""

    def __init__(self):
        pass

    @classmethod
    def Invoke(cls, url, method, *args):
        """
        接口webservice方法，返回结果
        :param url: webservice访问地址
        :param method: 方法名
        :param args: 调用接口使用的参数
        """
        try:
            print('Request: \t', args)
            imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
            imp.filter.add('http://' + url.split('/')[2])
            client = Client(url, doctor=ImportDoctor(imp))
            response = getattr(client.service, method)(*args)
            print('Response: \t', response)
            return response

        except Exception as e:
            print(e)
