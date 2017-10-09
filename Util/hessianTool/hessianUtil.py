# coding:utf-8

from pyhessian.client import HessianProxy
from pyhessian import protocol
import json
import time
import datetime
from ..commonTool import *


def FormatObject(obj):
    try:
        if hasattr(obj, '__dict__'):
            if '_Object__meta_type' in obj.__dict__:
                obj.__dict__.pop('_Object__meta_type')
            obj = obj.__dict__
            for i in obj.keys():
                if hasattr(obj[i], '__dict__') or hasattr(obj[i], 'has_key'):
                    obj[i] = FormatObject(obj[i])
                elif hasattr(obj[i], '__iter__'):
                    obj[i] = [FormatObject(j) for j in obj[i]]
                elif hasattr(obj[i], 'time'):
                    obj[i] = obj[i].strftime("%Y-%m-%d %H:%M:%S")
            return obj

        elif hasattr(obj, 'has_key'):
            for i in obj.keys():
                if hasattr(obj[i], '__dict__') or hasattr(obj[i], 'has_key'):
                    obj[i] = FormatObject(obj[i])
                elif hasattr(obj[i], '__iter__'):
                    obj[i] = [FormatObject(j) for j in obj[i]]
                elif hasattr(obj[i], 'time'):
                    obj[i] = obj[i].strftime("%Y-%m-%d %H:%M:%S")
            return obj

        return obj
    except Exception as e:
        print e


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print "Cost:\t%ss\r\n" % (time.clock() - t)
        return res
    return wrapper


class HessianUtil(object):
    def __init__(self):
        pass

    @classmethod
    @benchmark
    def Invoke(cls, method, *req, **kwargs):
        try:
            def date_handler(obj): return (
                obj.isoformat()
                if isinstance(obj, datetime.datetime)
                or isinstance(obj, datetime.date)
                else None
            )

            confSection = kwargs.get('confSection', 'Dubbo')
            confFile = kwargs.get('confFile', '/config/test.yml')
            host = ConfigUtil.get(confSection, 'Host', confFile)
            port = ConfigUtil.get(confSection, 'Port', confFile)
            service = ConfigUtil.get(confSection, 'Service', confFile)
            interface = ConfigUtil.get(confSection, 'Interface', confFile)
            url = host + ':' + port + '/' + service + '.' + interface

            print '\r\nInvoke Hessian Interface:\r\nURL:\t', url
            print 'Method:\t', method
            res = FormatObject(getattr(HessianProxy(url, timeout=60), method)(*req))
            print 'Req:\t', [FormatObject(i) for i in req]
            print 'Res:\t', json.dumps(res, default=date_handler, ensure_ascii=False)
            return res

        except Exception as e:
            print e
