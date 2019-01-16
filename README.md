# Taffy

Taffy is a Test Automation Framework based on nosetests.

Taffy is usesd mainly to test interface including Http, dubbo/hessian, Webservice, Socket and etc.

Taffy also provided encapsulation and realized the interfaces of data check, config read, DB / redis operations, data encryption / decryption and etc.

The basic useage can be found at Tests/ folder.

Taffy是基于nosetests的自动化测试框架。

Taffy主要适用于服务端接口(包含且不限于Http, Dubbo/hessian, Webservice, Socket等协议)功能及性能自动化测试；也可集成Selenium, Appium进行WEB或APP的自动化测试。

Taffy同时封装实现了配置读取、数据对比、DB/Redis操作、数据加解密、正交表生成测试用例等工具类。

基本用法可以参考[Tests/](https://github.com/lovesoo/Taffy/tree/master/Tests)目录。

欢迎加入QQ群交流讨论：[25452556](https://jq.qq.com/?_wv=1027&k=5pqB0UV)

# 目录
- [Taffy](#taffy)
- [0. 更新记录](#0-更新记录)
- [1. 运行环境](#1-运行环境)
- [2. 项目结构](#2-项目结构)
- [3. 环境部署](#3-环境部署)
    - [3.1 Python](#31-python)
    - [3.2 IDE](#32-ide)
    - [3.3 Lib](#33-lib)
    - [3.4 PyCharm配置](#34-pycharm配置)
- [4. 测试编写执行及报告导出](#4-测试编写执行及报告导出)
    - [4.1 功能自动化测试](#41-功能自动化测试)
        - [4.1.1 测试编写](#411-测试编写)
        - [4.1.2 测试执行](#412-测试执行)
        - [4.1.3 测试报告](#413-测试报告)
    - [4.2 性能测试](#42-性能测试)
        - [4.2.1 配置config/locust.yml](#421-配置configlocustyml)
        - [4.2.2 运行locust](#422-运行locust)
        - [4.2.3 测试报告](#423-测试报告)
- [5. 参考资料](#5-参考资料)
- [6. 联络方式](#6-联络方式)
- [7. 附录](#7-附录)
    - [7.1 locust框架集成使用说明](#71-locust框架集成使用说明)
    - [7.2 nose编写测试用例方法](#72-nose编写测试用例方法)
    - [7.3 Jenkins集成](#73-jenkins集成)

# 0. 更新记录

20181010 v1.7 Python 3.7版本适配，现已支持Python2.7 - 3.7

20171030 v1.6 支持模块自定义配置安装，详见[**setup.py**](https://github.com/lovesoo/Taffy/blob/master/setup.py)

20171015 v1.5 新增《[**Taffy入门教学视频**](http://v.youku.com/v_show/id_XMzA4NTk2MDI5Mg==.html)》

20171010 v1.4 支持分布式模式运行locust

20171009 v1.3 统一配置文件格式为YAML

20170928 v1.2 集成locust，相同脚本可同时进行功能自动化及性能测试，详见[**附录7-1**](#71-locust框架集成使用说明)

20170922 v1.1 集成selenium，新增相关测试demo

20170920 v1.0 发布第一个版本，支持http/hessian/webservice等类型接口功能自动化测试，并提供相关Util工具类

# 1. 运行环境
- macOS，linux，windows
- nose 1.3.7
- python 2.7 - 3.7

# 2. 项目结构
1) config 配置文件
2) Tests 测试用例
3) Util 工具类
    - checkTool 数据比较
    - commonTool    配置文件读取
    - DBTool    数据库操作
    - hessianTool   hessian接口
    - httpTool  http接口
    - locustTool    locust集成
    - OATool    正交表设计测试用例
    - redisTool redis/redis cluster操作
    - securityTool  数据加解密
    - seleniumTool  selenium集成
    - webserviceTool    webservice接口

# 3. 环境部署
## 3.1 Python

请根据需要下载Python 2.7或3.7版本：

```
https://www.python.org/downloads/
```


## 3.2 IDE

推荐使用PyCharm：

```
官网地址：http://www.jetbrains.com/pycharm/
```


## 3.3 Lib

[requirements.txt ](https://github.com/lovesoo/Taffy/blob/master/requirements.txt)中存放了Taffy用到的第三方lib库，可以运行[` python setup.py`](https://github.com/lovesoo/Taffy/blob/master/setup.py)进行模块安装配置，命令如下：

```
# 默认安装全部模块
$ python setup.py

# -h或--help，查看帮助
$ python setup.py -h
```

## 3.4 PyCharm配置

1) 运行PyCharm，打开下载的项目：taffy

2) 「File」–>「Settings 」–>「Project:Taffy」->「Project Interpreter」，配置Python interpreter为当前python版本安装目录

3) 「File」–>「Settings 」–>「Tools」->「Python Integrated Tools」–>「Nosetests」，配置Default test runner为Nosetests

4) 「Run」–>「Edit Configurations」–>「Defaults」->「Python」，配置Python interpreter为当前python版本安装目录

5)  「Run」–>「Edit Configurations」–>「Defaults」->「Python tests」–>「Nosetests」，配置Python interpreter为当前python版本安装目录，并在Interpreter options中填入-s用以显示nose运行及调试信息

# 4. 测试编写执行及报告导出
## 4.1 功能自动化测试

### 4.1.1 测试编写

taffy目前只支持nose方式编写测试用例，详见[附录7-2](#72-nose编写测试用例方法)

后续可扩展支持其他方式，如以excel,csv,yaml等数据驱动形式保存用例

### 4.1.2 测试执行

可以使用两种方式执行功能自动化测试脚本：

1) 图形用户界面GUI

    在PyCharm中，选中测试文件，如Tests/test_demo.py

    鼠标右键选择Run 'Nosetests in test_demo.py'即可执行测试

    注1：也可使用快捷键：Ctrl+Shift+F10

    注2：在脚本里使用快捷键Ctrl+Shift+F10，会单独执行选中的test class或test func

2) 命令行界面CLI

在PyCharm下方Terminal终端中，输入命令执行测试：

```
# 执行测试文件test_demo.py
$ nosetests -v Tests/test_demo.py

# 单独执行测试文件test_demo.py中测试类test_demo下的test_http测试方法
$ nosetests -v Tests/test_demo.py:test_demo.test_http
```
更多nosetests运行选项，请参考[nostests官方文档](http://nose.readthedocs.io/en/latest/man.html)

### 4.1.3 测试报告

功能自动化测试执行完成后，在Pycharm左下方Run窗口的Testing toolbar中，选择“Export Test Results”按钮即可导出测试报告

详见[《PyCharm运行Nosetests并导出测试报告》](http://lovesoo.org/pycharm-run-nosetests-and-exports-test-report.html)

## 4.2 性能测试

### 4.2.1 配置config/locust.yml

### 4.2.2 运行locust

运行test_locust.py生成locustfile及执行性能测试，命令如下：

```
$ cd Taffy\Tests
$ python test_locust.py
```

### 4.2.3 测试报告

1) 普通模式

    locust以普通模式运行时，可在[web页面](http://localhost:8089/)实时查看运行结果，包括请求数，响应时间，RPS，失败率等

    测试执行完成后可在WEB页面下载CSV格式测试报告（选择Download Data -> Download response time distribution CSV）

2) no-web模式

    locust以no-web模式运行时，csv格式数据会定时保存在运行目录下，如locust_distribution.csv和locust_requests.csv

Taffy集成locust性能测试框架使用说明，详见[附录7-1](#71-locust框架集成使用说明)


# 5. 参考资料

1. http://nose.readthedocs.io/en/latest/index.html

2. https://docs.python.org/dev/library/unittest.html

3. https://docs.locust.io/en/latest/

4. http://www.cnblogs.com/yufeihlf/p/5764099.html


# 6. 联络方式

QQ交流群：[25452556](https://jq.qq.com/?_wv=1027&k=5pqB0UV)


# 7. 附录

## 7.1 locust框架集成使用说明

[《Taffy集成Locust性能测试框架使用说明》](http://lovesoo.org/taffy-using-locust-performance-testing.html)

## 7.2 nose编写测试用例方法

[《nose框架编写测试用例方法》](http://lovesoo.org/nose-writing-tests.html)

## 7.3 Jenkins集成

[《Jenkins集成taffy进行自动化测试并输出测试报告》](http://lovesoo.org/jenkins-integrated-taffy-for-automated-testing-and-output-test-reports.html)