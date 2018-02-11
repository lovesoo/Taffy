# Taffy

Taffy is a Test Automation Framework based on nosetests.

Taffy is usesd mainly to test interface including Http, dubbo/hessian, Webservice, Socket and etc.

Taffy also provided encapsulation and realized the interfaces of data check, config read, DB / redis operations, data encryption / decryption and etc.

The basic useage can be found at Tests/ folder.

Taffy是基于nosetests的自动化测试框架。

Taffy主要用来测试后台服务(包含且不限于Http, Dubbo/hessian, Webservice, Socket等协议接口)、也可集成Selenium, Appium进行WEB或APP的自动化测试、或集成locust进行性能测试。

Taffy同时封装实现了配置读取、数据对比、DB/Redis操作、数据加解密等接口。

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
- python 2.7

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
    - redisTool redis操作（支持redis cluster）
    - securityTool  数据加解密
    - seleniumTool  selenium集成
    - webserviceTool    webservice接口

# 3. 环境部署
## 3.1 Python

请下载安装Python2.7.x版本：

```
https://www.python.org/downloads/
```


## 3.2 IDE

推荐使用PyCharm：

```
官网地址：http://www.jetbrains.com/pycharm/

下载安装完成后，注册时选择License server,输入：http://idea.imsxm.com

即可激活^^
```


## 3.3 Lib

[requirements.txt ](https://github.com/lovesoo/Taffy/blob/master/requirements.txt)中存放了Taffy用到的第三方lib库，可以运行[` python setup.py`](https://github.com/lovesoo/Taffy/blob/master/setup.py)进行模块安装配置，命令如下：

```
# 默认安装全部模块
$ python setup.py
```

详细用法如下：

```
# 默认安装全部模块
$ python setup.py

# -m或--min，最小化安装（只安装必须的nose,requests,PyYAML等）
$ python setup.py -m

# -w或--without A B，不安装模块A,B
# 示例：不安装db redis locust模块
$ python setup.py --without db redis locust

# --with A B,在最小化安装基础上，只安装模块A,B
# 示例：只安装db redis locust模块
$ python setup.py --with db redis locust

# 其中，--with及--without选项支持的模块列表为：[redis,security,db,webservice,selenium,locust,hessian]

# -h或--help，查看帮助
$ python setup.py -h
```

Windows系统一些报错Lib安装方法:

1) mysql-python

    1) 首先安装Microsoft Visual C++ Compiler for Python 2.7：http://aka.ms/vcpython27

    2) 然后下载msi包安装：https://sourceforge.net/projects/mysql-python/files/mysql-python/1.2.3/

2) pymssql

    可直接下载exe包安装: https://pypi.python.org/pypi/pymssql/2.1.1#downloads

    python2.7+32位windows系统，请选择：pymssql-2.1.1.win32-py2.7.exe (md5)

3) webdriver

    这里只说下chromedriver的下载配置方法：
    1. 下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads

    2. 下载chromedriver_win32.zip，解压后将chromedriver.exe放到Python安装路径下（如C:\Python27\）

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

后续若有需求，可扩展支持其他方式，如以excel,csv,yaml等数据驱动形式保存用例

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
### 7.1.1 简介
Locust是使用Python语言编写实现的开源性能测试工具，简洁、轻量、高效，并发机制基于gevent协程，可以实现单机模拟生成较高的并发压力。

官网：https://locust.io/

主要特点如下：
1. 使用普通的Python脚本用户测试场景
2. 分布式和可扩展，支持成千上万的用户
3. 基于Web的用户界面，用户可以实时监控脚本运行状态
4. 几乎可以测试任何系统，除了web http接口外，还可自定义clients测试其他类型系统


### 7.1.2 安装
可以使用pip快速安装Locust：

```
pip install locustio
```

### 7.1.3 使用
taffy集成locust的基本流程如下：

1) 配置config/locust.yml

    YAML是对人友好的数据序列化标准，可适用所有的编程语言。
    与json相互在线转换网站：https://www.json2yaml.com/

    可以使用pip安装PyYAML：

    ```
    pip install PyYAML
    ```

    locust.yml主要配置项如下：

    a) mode 运行模式

    为0表示单例模式；

    为1表示分布式，使用可选参数slaves_num,master_port

    b) no-web 是否以no-web模式运行

    为0表示普通模式，使用可选参数port；运行后需要先手工在浏览器打开[locust 页面](http://localhost:8089/)，填入并发用户数及每秒请求数后再执行测试

    为1表示no-web模式，使用可选参数csv,c,r,run_time

    c) min_wait及max_wait，可选参数，表示任务执行之间最小及最大等待时间（默认值分别为100/1000，单位ms）

    d) task为测试任务配置：必填参数file,class,function分别代表测试文件，类及方法；可选参数weight（默认值1）

    特别注意：使用nose独有的[Test generators](http://nose.readthedocs.io/en/latest/writing_tests.html#test-generators)方法编写的Tests,转换为locustfile后Locust无法正常执行性能测试（运行结果为空），故这里填写的class/function暂不支持使用Test generators方法编写

    locust.yml示例如下：

    ```
    ---
    #mode 运行模式（默认为0） 0:单例模式; 1:分布式
    #no-web 是否以no-web模式运行（默认为0） 0:否; 1:是
    #min_wait/max_wait 任务执行之间的最小、最大等待时间（默认为10/1000ms）

    #只有mode为1时，params中如下参数才有效：slaves_num,master_port
      #slaves_num slaves数目（默认为当前机器cpu核数）
      #master_port master绑定端口号（默认5557）

    #只有no-web为0时，params中如下参数才有效：port
      #port web端口号，默认8089

    #只有no-web为1时，params中如下参数才有效：csv,c,r,run_time
      #csv 运行结果文件名
      #c 并发用户数
      #r 每秒请求数
      #run_time 运行时间
    mode: 1
    no_web: 1
    min_wait: 100
    max_wait: 1000
    params:
      slaves_num: 4
      master_port: 5557
      port: 8089
      csv: locust
      c: 10
      r: 10
      run_time: 5m
    #task 性能测试任务
    task:
      #file 测试文件名，支持相对路径如test_xxx/text_xxx_file.py
      #class 测试类
      #function 测试方法
      #weight 任务选择的概率权重（默认1）
    - file: test_demo.py
      class: test_demo
      function: test_httpbin_get
      weight: 2
    - file: test_demo.py
      class: test_demo
      function: test_httpbin_post
      weight: 1
    - file: test_demo.py
      class: test_demo
      function: test_webservice
      weight: 1
    ```

2) 根据配置文件locust.yml，读取模板生成locustfile文件，然后运行locust执行性能测试，命令如下：
    ```
    $ cd Taffy\Tests
    $ python test_locust.py
    ```

3) 与jmeter性能测试结果对比

    针对[百度首页搜索接口](https://www.baidu.com/s?wd=taffy)，分别使用jmeter及locust进行了10路并发性能测试（时间为5min）。

    jmeter性能测试统计结果如下：

    Label | # Samples | Average | Min | Max | Std.Dev. | Error % | Throughput
    ---|---|---|---|---|---|---|---
    test_baidu | 1173 | 2539 | 1424 | 5856 | 617 | 0.0 | 3.9

    locust性能测试统计结果如下：

    Name | #reqs | #fails | Avg | Min | Max | Median | req/s
    ---|---|---|---|---|---|---|---
    test_baidu | 1248 | 0(0.00%) | 2390 | 1140 | 4094 | 2400 | 4.2

    可以看出针对百度搜索接口进行5min的10路并发性能测试，jmeter及locust总体请求数分别为1173及1248，平均响应时间分别为2.539s及2.390s，每秒请求数分别为3.9及4.2。

    可以得出结论：**locust与jmeter性能测试结果基本一致。**

## 7.2 nose编写测试用例方法

[《nose框架编写测试用例方法》](http://lovesoo.org/nose-writing-tests.html)

## 7.3 Jenkins集成

[《Jenkins集成taffy进行自动化测试并输出测试报告》](http://lovesoo.org/jenkins-integrated-taffy-for-automated-testing-and-output-test-reports.html)