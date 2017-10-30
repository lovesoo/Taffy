# coding:utf-8
import sys
import os

# Taffy运行lib库自定义配置安装
# 默认全部安装，可选最小配置 -m，或选择只需 --with /不需安装 --without的模块
# 可自选只需/不需安装的模块列表[redis,security,db,webservice,selenium,locust,hessian]
# 更多帮助请查看：python setup.py --help


def markfile(modules=[], mark=True):
    try:
        # 注释/解除注释模块
        if not modules:
            for tfile in [init_file, requirements_file]:
                lines = open(tfile, 'r').readlines()
                flen = len(lines)
                for i in range(flen):
                    if '#' not in lines[i] and mark:
                        lines[i] = lines[i].replace(lines[i], '#' + lines[i])
                    elif '#' in lines[i] and not mark:
                        lines[i] = lines[i].replace(lines[i], lines[i].strip('#'))
                open(tfile, 'w').writelines(lines)
        else:
            if 'security' in modules:
                modules.append('pycrypto')
            if 'db' in modules:
                modules.append('sql')
            if 'webservice' in modules:
                modules.append('suds')

            for tfile in [init_file, requirements_file]:
                for module in modules:
                    lines = open(tfile, 'r').readlines()
                    flen = len(lines)
                    for i in range(flen):
                        if '#' not in lines[i] and mark and module.lower() in lines[i].lower():
                            lines[i] = lines[i].replace(lines[i], '#' + lines[i])
                        elif '#' in lines[i] and not mark and module.lower() in lines[i].lower():
                            lines[i] = lines[i].replace(lines[i], lines[i].strip('#'))
                    open(tfile, 'w').writelines(lines)
    except Exception as e:
        print e


if __name__ == '__main__':
    requirements_file = 'requirements.txt'
    init_file = 'Util/__init__.py'
    ROOT = os.path.abspath(os.path.dirname(__file__))
    requirements_file = os.path.join(ROOT, requirements_file)
    init_file = os.path.join(ROOT, init_file)
    all_modules = ['redis', 'security', 'db', 'webservice', 'selenium', 'locust', 'hessian']

    # 默认安装所有模块
    markfile(mark=False)
    if len(sys.argv) < 2:
        print 'Taffy setup with all modules.'
    elif '-m' == sys.argv[1] or 'min'in sys.argv[1]:
        print 'Taffy setup with the minimum modules.'
        markfile(all_modules)
    elif '-w' == sys.argv[1] or 'without' in sys.argv[1]:
        if all([m in all_modules for m in sys.argv[2:]]):
            print 'Taffy setup without the modules:', sys.argv[2:]
            markfile(sys.argv[2:])
        else:
            print '{0} not all in the supported modules list {1}'.format(sys.argv[2:], all_modules)
    elif '-with' == sys.argv[1] or '--with' == sys.argv[1]:
        if all([m in all_modules for m in sys.argv[2:]]):
            print 'Taffy setup with the modules:', sys.argv[2:]
            markfile([m for m in all_modules if m not in sys.argv[2:]])
        else:
            print '{0} not all in the supported modules list {1}'.format(sys.argv[2:], all_modules)
    elif '-h' == sys.argv[1] or 'help' in sys.argv[1]:
        print 'Taffy setup.py help document.'
        print 'Usage: python setup.py [options]'
        print 'Options:'
        print '\t-h, --help\tshow this help message and exit'
        print '\t-m, --min\tsetup with the minimum modules'
        print '\t-w module A [module B...], --without module A [module B...]\tsetup without the modules, eg "--without redis security db".'
        print '\t--with module A [module B...]\tsetup only with the modules, eg "--with redis security db".'
        print '\t\tSupported setup with/without modules are [redis,security,db,webservice,selenium,locust,hessian]'
    else:
        assert False, 'Not supported option and see --help for available options.'

    os.system('pip install -r {0}'.format(requirements_file))
