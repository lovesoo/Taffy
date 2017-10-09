# coding=utf-8

import json
import requests
from ..commonTool import *


def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv


def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
            key = key.encode('utf-8')
            value = value.encode('utf-8')
        elif isinstance(value, list):
            value = _decode_list(value)
        elif isinstance(value, dict):
            value = _decode_dict(value)
        rv[key] = value
    return rv


class HttpUtil(object):
    '''基础调用类，包括基本的http method'''

    @classmethod
    def get(cls, name, confSection='Http', confFile='/config/test.yml', **kwargs):
        """http get method

        :param params: 接口参数
        :type params: dict
        :param name: 接口名
        :type name: string
        :param confSection: 配置名，根据配置名去配置文件读取相应的配置
        :type confSection: string
        """

        host = ConfigUtil.get(confSection, 'Host', confFile)
        port = ConfigUtil.get(confSection, 'Port', confFile)
        path = ConfigUtil.get(confSection, 'Path', confFile)

        url = host + ':' + port + path + name

        response = requests.get(url, **kwargs)
        response.raise_for_status()
        return response

    @classmethod
    def post(cls, name, confSection='Http', confFile='/config/test.yml', **kwargs):
        """http post methode
        :param params: 接口queryString
        :type params: dict
        :param body: 接口 post body
        :type body: string
        :param name: 接口名
        :type name: string
        :param confSection: 配置名，根据配置名去配置文件读取相应的配置
        :type confSection: string
        """
        host = ConfigUtil.get(confSection, 'Host', confFile)
        port = ConfigUtil.get(confSection, 'Port', confFile)
        path = ConfigUtil.get(confSection, 'Path', confFile)

        url = host + ':' + port + path + name
        response = requests.post(url, **kwargs)
        response.raise_for_status()

        return response


class BaiduHttpUtil(object):
    """百度搜索调用类"""

    def __init__(self, ):
        pass

    @classmethod
    def get(cls, name, srequest):
        params = srequest.GetDict()
        print 'Request:\t', json.dumps(params, ensure_ascii=False)
        response = HttpUtil.get(name, params=params)
        print 'Response:\t', response
        return response.text


class HttpbinUtil(object):
    """httpbin通用调用类"""
    confSection = 'Httpbin'

    def __init__(self, ):
        pass

    @classmethod
    def get(cls, name, srequest):
        params = srequest.GetDict()
        print 'Request:\t', json.dumps(params, ensure_ascii=False)
        response = HttpUtil.get(name, cls.confSection, params=params)
        print 'Response:\t', response.text
        return response.json()

    @classmethod
    def post(cls, name, srequest):
        params = srequest.GetDict()
        print 'Request:\t', json.dumps(params, ensure_ascii=False)
        response = HttpUtil.post(name, cls.confSection, data=params)
        print 'Response:\t', response.text
        return response.json()
