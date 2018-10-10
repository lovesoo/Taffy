# coding=utf-8
from nose.tools import *
import json


def is_json(json_str):
    try:
        json.loads(json_str)
    except (ValueError, TypeError):
        return False
    return True


class CheckUtil(object):
    @staticmethod
    def check(expr, msg=None):
        """检查表达式expr是否为True，如果为False，则抛出异常并显示消息msg
        :param expr: 表达式
        :type expr: expression
        :param msg: 消息
        :type msg: string
        """
        ok_(expr, msg)

    @staticmethod
    def check_return(data):
        """检查返回值是否正确
        :param data: 接口返回包的result部分
        :type data: json对象
        """
        eq_(data['returncode'], '0000', '%s: ' % data['returncode'] + data['returndesc'])

    @staticmethod
    def check_equal(a, b, msg=''):
        fmsg = ': %r != %r ' % (a, b)
        eq_(a, b, msg + fmsg)

    @staticmethod
    def check_dict(data, jsondata, columns=None, keymaps=None):
        """检查两个字典是否相等
        :rtype: object
        :param data: 字典数据
        :type data: 字典或json对象
        :param jsondata: json数据
        :type jsondata: json对象
        :param columns: data中需要检查的key，空表示检查所有key
        :type columns: list
        :param keymaps: data和jsondata中可能有某些key名字不同，keymaps就是key的对应关系，空表示检查所有key
        :type keymaps: dict
        """
        if columns is None:
            columns = []
        if keymaps is None:
            keymaps = {}
        if isinstance(data, tuple):
            if len(data) != len(jsondata):
                assert False, 'len not equal, data=%s, jsondata=%s' % (data, jsondata)
            i = 0
            while i < len(data):
                if not CheckUtil.check_dict(data[i], jsondata[i], columns, keymaps):
                    assert False, 'not equal, data=%s, jsondata=%s' % (data[i], jsondata[i])
                i += 1
            return True
        elif isinstance(data, list):
            i = 0
            while i < len(data):
                if not CheckUtil.check_dict(data[i], jsondata[i], columns, keymaps):
                    assert False, 'not equal, data=%s, jsondata=%s' % (data[i], jsondata[i])
                i += 1
            return True
        elif isinstance(data, dict):
            for key in data:
                if not columns:
                    if not keymaps.get(key, key) in jsondata:
                        assert False, 'key: %s not in jsondata=%s' % (keymaps.get(key, key), jsondata)
                    else:
                        if not CheckUtil.check_dict(data[key], jsondata[keymaps.get(key, key)], columns, keymaps):
                            assert False, 'not equal, data=%s, jsondata=%s' % (data[key], jsondata[keymaps.get(key, key)])
                else:
                    if key not in columns:
                        continue
                    else:
                        if not keymaps.get(key, key) in jsondata:
                            assert False, 'key: %s not in jsondata=%s' % (keymaps.get(key, key), jsondata)
                        else:
                            if not CheckUtil.check_dict(data[key], jsondata[keymaps.get(key, key)], columns, keymaps):
                                assert False, 'not equal, data=%s, jsondata=%s' % (data[key], jsondata[keymaps.get(key, key)])
            return True
        else:
            if isinstance(jsondata, str):
                jsondata = jsondata.encode('utf-8')
            if isinstance(data, str):
                data = data.encode('utf-8')
            try:
                assert data == jsondata, '%s != %s' % (data, jsondata)
                return data == jsondata
            except AssertionError:
                if is_json(data):
                    data = json.loads(data)
                    if not CheckUtil.check_dict(data, jsondata, columns, keymaps):
                        assert False, 'not equal, data=%s, jsondata=%s' % (data, jsondata)
                    return True
                else:
                    return False


if __name__ == '__main__':
    data = dict(returncode='0000', returndesc='success')
    jsondata = {'returncode': '0000', 'returndesc': 'success'}

    CheckUtil().check(1 == 1)
    CheckUtil().check_return(data)
    CheckUtil().check_equal('a', 'a')
    CheckUtil().check_dict(data, jsondata)
