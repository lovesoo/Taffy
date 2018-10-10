# coding=utf-8
import os
import sys
import io
import inspect
import yaml


def GetPath(module=None):
    """获取当前模块所在路径"""
    if not module:
        module = GetPath
    cur_module = inspect.getmodule(module)
    path = os.path.dirname(cur_module.__file__)
    return path


ROOT = os.path.abspath(os.path.join(GetPath(sys.modules['Util']), os.path.pardir))
# ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))


class ConfigUtil(object):

    @classmethod
    def getall(cls, path='/config/test.yml'):
        """获取配置文件中的配置，返回string"""
        filepath = ROOT + path
        return yaml.load(io.open(filepath, 'r', encoding='utf-8'))

    @classmethod
    def get(cls, section, option='', path='/config/test.yml'):
        """获取配置文件中的配置，返回string"""
        filepath = ROOT + path
        config = yaml.load(io.open(filepath, 'r', encoding='utf-8'))
        if option:
            result = config[section][option]
        else:
            result = config[section]
        return str(result) if isinstance(result, (str, int)) else result

    @classmethod
    def getint(cls, section, option='', path='/config/test.yml'):
        """获取配置文件中的配置，返回int"""
        filepath = ROOT + path
        config = yaml.load(io.open(filepath, 'r', encoding='utf-8'))
        if option:
            return int(config[section][option])
        else:
            return int(config[section])


if __name__ == '__main__':
    print(ConfigUtil.getall('/config/selenium.yml'))
