# coding=utf-8
import os
import inspect
import ConfigParser
import sys


def GetPath(module=None):
    """获取当前模块所在路径"""
    if not module:
        module = GetPath
    cur_module = inspect.getmodule(module)
    path = os.path.dirname(cur_module.__file__)
    return path


ROOT = GetPath(sys.modules['Util']) + '/..'


class ConfigUtil(object):
    @classmethod
    def get(cls, section, option, path='/config/test.conf'):
        """获取配置文件中的配置，返回string"""
        filepath = ROOT + path
        cf = ConfigParser.ConfigParser()
        cf.read(filepath)

        return cf.get(section, option)

    @classmethod
    def getInt(cls, section, option, path='/config/test.conf'):
        """获取配置文件中的配置，返回int"""
        filepath = ROOT + path
        cf = ConfigParser.ConfigParser()
        cf.read(filepath)

        return cf.getint(section, option)
