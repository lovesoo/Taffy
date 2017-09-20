# coding=utf-8
import sys
import os
import re
import copy


class BaseUtil(object):
    def __init__(self, connection):
        """Constructor"""
        self.connection = connection
        self.cursor = None

    def execute(self, sql, params=()):
        """"""
        if self.isQuery(sql):
            return self.executeQuery(sql, params)
        else:
            return self.executeNonQuery(sql, params)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def isQuery(self, sql):
        copy_sql = copy.copy(sql)
        if re.search('select ', copy_sql.lstrip(), re.IGNORECASE):
            return True
        else:
            return False

    def executeQuery(self, sql, params=()):
        raise NotImplementedError

    def executeNonQuery(self, sql, params=()):
        return NotImplementedError
