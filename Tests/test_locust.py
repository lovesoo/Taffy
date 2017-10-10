# coding:utf-8
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Util import *
import multiprocessing


def start_slave(locust_file):
    print 'start slave pid:\t{0}'.format(os.getpid())
    os.system('locust -f {0} --slave'.format(locust_file))


if __name__ == '__main__':
    multiprocessing.freeze_support()
    LU = locustUtil()
    # 读取配置config/locust.yml，生成locustfile.py
    locust_file = LU.genLocustfile()
    # 生成locust运行命令
    locust_command = LU.getRunCommand()

    # 运行locust
    if locust_command:
        if 'master' in locust_command:
            # 分布式
            num = LU.cases['params'].get('slaves_num', multiprocessing.cpu_count())
            record = []
            for i in range(num):
                process = multiprocessing.Process(target=start_slave, args=(locust_file,))
                process.start()
                record.append(process)

            print 'start master pid:\t{0}'.format(os.getpid())
            cmd = 'locust -f {0} {1}'.format(locust_file, locust_command)
            print 'cmd:\t{0}'.format(cmd)
            os.system(cmd)
        else:
            # 单例模式，no-web
            cmd = 'locust -f {0} {1}'.format(locust_file, locust_command)
            print 'cmd:\t{0}'.format(cmd)
            os.system(cmd)
    else:
        # 单例模式，web
        cmd = 'locust -f {0}'.format(locust_file)
        print 'cmd:\t{0}'.format(cmd)
        os.system(cmd)
