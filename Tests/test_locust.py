# coding:utf-8
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Util import *


if __name__ == '__main__':
    LU = locustUtil()
    # 读取配置文件config/locust.yml
    # 生成locustfile.py
    locust_file = LU.genLocustfile()

    # 生成locust运行命令
    locust_command = LU.getRunCommand()

    # 运行locust
    if locust_command:
        os.system('locust -f {0} {1}'.format(locust_file, locust_command))
    else:
        os.system('locust -f {0}'.format(locust_file))
