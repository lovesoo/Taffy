# coding=utf-8
import sys
import os
import pymysql
import pymssql
from DBUtils import PooledDB
from .mysqlUtil import *
from ..commonTool import *


class DBUtil(object):
    """数据库工具类，提供连接池以及执行sql语句的方法,目前支持mysql及sqlserver"""
    pools = {}

    def __init__(self):
        pass

    @classmethod
    def getCon(cls, confSection, confFile='/config/test.yml'):
        """创建连接池，并从池中返回对应的数据库处理工具类
        :param confSection: 配置名
        :type confSection: string
        :param database: 数据库名
        :type database: string
        """
        database = ConfigUtil.get(confSection, 'Database', confFile)
        key = confSection + ':' + database
        clz = ''
        if key not in cls.pools:
            dbType = ConfigUtil.get(confSection, 'Type', confFile)
            mincached = 10
            maxcached = 20
            maxshared = 15
            if dbType == 'mysql':
                conf = ConfigUtil.get(confSection, path=confFile)
                host = conf.get('Host')
                port = conf.get('Port')
                user = conf.get('User')
                pwd = conf.get('Passwd')
                charset = conf.get('charset', 'utf8')

                dbParam = {'host': host, 'port': port, 'user': user, 'passwd': pwd, 'db': database, 'charset': charset, 'cursorclass': pymysql.cursors.DictCursor}
                pool = PooledDB.PooledDB(pymysql, mincached, maxcached, maxshared, **dbParam)
                clz = MysqlUtil
                cls.pools[key] = (pool, clz)
            else:
                raise NotImplementedError

        databasePool = cls.pools[key][0]
        clz = cls.pools[key][1]

        return clz(databasePool.connection())

    @classmethod
    def execute(cls, sql, params=(), confSection='Mysql', confFile='/config/test.yml'):
        """执行mysql语句，支持动态语法
        :param sql: mysql语句，动态语法时包含占位符%s
        :type sql: string
        :param params: 如果为动态语句，为动态参数的数组，数组长度与sql中的占位符个数一致
        :type params: list
        :param database: 数据库名
        :type database: string
        :param confSection: 配置名，根据配置名去配置文件读取相应的配置
        :type confSection: string
        :param confSection: 配置文件
        :type confSection: string
        """
        try:
            data = []
            instance = cls.getCon(confSection, confFile)
            data = instance.execute(sql, params)
        except Exception as e:
            print(e)
        finally:
            instance.close()
            return data
