# Taffy

Taffy is a Test Automation Framework based on nosetests.

Taffy is usesd mainly to test interface including Http, dubbo/hessian, Webservice, Socket and etc.

Taffy also provided encapsulation and realized the interfaces of data check, config read, DB / redis operations, data encryption / decryption and etc.

The basic useage can be found at Tests/test_demo.py.

Taffy是基于nosetests的自动化测试框架.

Taffy主要用来测试后台服务(包括且不限于Http, Dubbo/hessian, Webservice, Socket等类型接口)，也可集成Selinum, Appium进行WEB或APP的自动化测试。

Taffy封装实现了结果对比，配置读取，DB/Redis操作，数据加解密等接口。

基本用法可以参考Tests/test_demo.py.

## 1. 运行环境
- macOS，linux，windows
- nose 1.3.7
- python 2.7

## 2. 结构介绍
1) config 配置文件
2) Tests 测试用例
3) Util 工具类
    - checkTool 比较方法及结果校验
    - commonTool    配置文件读取
    - DBTool    数据库操作(mysql,sqlserver)
    - hessianTool   hessian接口调用
    - httpTool  http接口调用
    - OATool    正交表设计测试用例
    - redisTool redis操作（支持redis及redis cluster）
    - securityTool  数据加解密
    - seleniumTool  selenium PageObject对象封装
    - webserviceTool    webservice接口调用

## 3. 使用方法
1) IDE

    推荐使用PyCharm

    ```
    官网地址：http://www.jetbrains.com/pycharm/

    下载安装完成后，注册时选择License server,输入：http://idea.imsxm.com

    即可激活^^
    ```


2) 安装第三方lib库

    使用pip install可以安装大多数的lib库：

    ```
    #可以单独安装lib库
    pip install xxxlib

    #也可以批量安装
    pip install -r requirements.txt
    ```

    一些棘手的lib库安装方法:

    1) mysql-python

        1) 首先安装Microsoft Visual C++ Compiler for Python 2.7：http://aka.ms/vcpython27

        2) 然后下载msi包安装：https://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.3/

    2) pymssql

        直接下载exe包安装: https://pypi.python.org/pypi/pymssql/2.1.1#downloads

        python2.7 32位windows系统请选择：pymssql-2.1.1.win32-py2.7.exe (md5)

    3) pyhessian

        Github地址：https://github.com/theatlantic/python-hessian

        下载zip包,解压后进行文件夹内，运行如下命令安装

        ```
        python setup.py install
        ```

3) PyCharm配置

    1) 「File」–>「open」，打开下载的项目taffy

    2) 「Run」–>「Edit Configurations」–>「Defaults」->「Python」，配置Python interpreter为当前python版本安装目录

    3)  「Run」–>「Edit Configurations」–>「Defaults」->「Python tests」–>「Nosetests」，Python interpreter为当前python版本安装目录，并在Interpreter options中填入-s用以显示nose运行及调试信息

4) 执行测试用例

    1) 选中Tests/test_demo.py

    2) 鼠标右键选择Run 'Nosetests in test_demo.py'即可执行测试

    3) 也可使用快捷键执行测试：Ctrl+Shift+F10

        注：在脚本中使用快捷键Ctrl+Shift+F10，会单独执行选中的test class下的一个test func

## 4.参考资料

    1. http://nose.readthedocs.io/en/latest/index.html

    2. https://docs.python.org/dev/library/unittest.html

    3. http://www.cnblogs.com/yufeihlf/p/5764099.html


## 5.联络方式

    QQ交流群：25452556