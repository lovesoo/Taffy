# coding=utf-8

import json
from ..commonTool import *


class HttpParam(object):
    """接口参数构造类，一般分为base，param，qrybase三部分，格式为json或xml"""

    def __init__(self, **kwargs):
        """构造函数.
        :param 为key=value的形式
        """
        self.data = {
            "ie": "utf-8",
            "tn": "baidu",
            "wd": "lovesoo"
        }

        self.data.update(kwargs)

    def GetJson(self):
        """
        返回json字符串
        """
        return json.dumps(self.data, ensure_ascii=False, indent=4)

    def GetDict(self):
        """
        返回dict对象
        """
        return self.data
