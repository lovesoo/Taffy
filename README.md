# Taffy

Taffy is a Test Automation Framework based on nosetests.

Taffy is usesd mainly to test interface including Http, dubbo/hessian, Webservice, Socket and etc.

Taffy also provided encapsulation and realized the interfaces of data check, config read, DB / redis operations, data encryption / decryption and etc.

The basic useage can be found at Tests/ folder.

Taffy是基于nosetests的自动化测试框架。

Taffy主要用来测试后台服务(包括且不限于Http, Dubbo/hessian, Webservice, Socket等类型接口)，也可集成Selenium, Appium进行WEB或APP的自动化测试，或集成locust进行性能测试。

Taffy封装实现了结果对比，配置读取，DB/Redis操作，数据加解密等接口。

基本用法可以参考[Tests/目录](https://github.com/lovesoo/Taffy/tree/master/Tests)下示例demo.

QQ交流群：[25452556](https://jq.qq.com/?_wv=1027&k=5pqB0UV)

## 目录
- [Taffy](#taffy)
    - [0. 更新记录](#0-更新记录)
    - [1. 运行环境](#1-运行环境)
    - [2. 项目结构](#2-项目结构)
    - [3. 环境部署](#3-环境部署)
    - [4. 测试编写、执行及报告导出](#4-测试编写、执行及报告导出)
    - [5.参考资料](#5参考资料)
    - [6.联络方式](#6联络方式)
    - [7. 附录](#7-附录)
        - [7.1 locust框架集成使用说明](#71-locust框架集成使用说明)
            - [7.1.1.Locust简介](#711locust简介)
            - [7.1.2. 安装](#712-安装)
            - [7.1.3. 使用方法](#713-使用方法)
        - [7.2 nose编写测试用例方法](#72-nose编写测试用例方法)
        - [7.3 Jenkins集成taffy进行自动化测试并输出测试报告](#73-jenkins集成taffy进行自动化测试并输出测试报告)

## 0. 更新记录

20171030 v1.6 支持模块自定义配置安装，详见[**setup.py**](https://github.com/lovesoo/Taffy/blob/master/setup.py)

20171015 v1.5 新增《[**Taffy入门教学视频**](http://v.youku.com/v_show/id_XMzA4NTk2MDI5Mg==.html)》

20171010 v1.4 支持分布式模式运行locust

20171009 v1.3 统一配置文件格式为YAML

20170928 v1.2 集成locust，同一脚本可同时进行功能自动化及性能测试，详见[**附录7-1**](https://github.com/lovesoo/Taffy#71-locust框架集成使用说明)

20170922 v1.1 集成selenium，新增相关测试demo

20170920 v1.0 第一个版本发布，支持http/hessian/webservice等类型接口功能自动化测试，并提供相关Util工具类

## 1. 运行环境
- macOS，linux，windows
- nose 1.3.7
- python 2.7

## 2. 项目结构
1) config 配置文件
2) Tests 测试用例
3) Util 工具类
    - checkTool 比较方法及结果校验
    - commonTool    配置文件读取
    - DBTool    数据库操作(mysql,sqlserver)
    - hessianTool   hessian接口调用
    - httpTool  http接口调用
    - locustTool    locust性能框架
    - OATool    正交表设计测试用例
    - redisTool redis操作（支持redis及redis cluster）
    - securityTool  数据加解密
    - seleniumTool  selenium PageObject对象封装
    - webserviceTool    webservice接口调用

## 3. 环境部署
1) Python

    请下载安装Python2.7.x版本：

    ```
    https://www.python.org/downloads/
    ```


2) IDE

    推荐使用PyCharm

    ```
    官网地址：http://www.jetbrains.com/pycharm/

    下载安装完成后，注册时选择License server,输入：http://idea.imsxm.com

    即可激活^^
    ```


3) 第三方lib

    [requirements.txt ](https://github.com/lovesoo/Taffy/blob/master/requirements.txt)中存放了Taffy用到的第三方lib库，可以通过[setup.py](https://github.com/lovesoo/Taffy/blob/master/setup.py)进行最大化、最小化及自定义模块安装配置：

    ```
    # 默认最大化安装（安装全部模块）
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

    当默认最大化安装全部模块时，Windows系统下一些棘手的lib安装方法:

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

4) PyCharm配置

    1) 运行PyCharm，打开下载的项目：taffy

    2) 「File」–>「Settings 」–>「Project:Taffy」->「Project Interpreter」，配置Python interpreter为当前python版本安装目录

    3) 「File」–>「Settings 」–>「Tools」->「Python Integrated Tools」–>「Nosetests」，配置Default test runner为Nosetests

    4) 「Run」–>「Edit Configurations」–>「Defaults」->「Python」，配置Python interpreter为当前python版本安装目录

    5)  「Run」–>「Edit Configurations」–>「Defaults」->「Python tests」–>「Nosetests」，配置Python interpreter为当前python版本安装目录，并在Interpreter options中填入-s用以显示nose运行及调试信息

## 4. 测试编写、执行及报告导出
1) 功能自动化测试

    1) 测试用例编写

        taffy目前只支持nose方式编写测试用例，详见[附录7-2](https://github.com/lovesoo/Taffy#72-nose编写测试用例方法)

        后续若有需求，可扩展支持其他方式，如以excel,csv,yaml等数据驱动形式保存用例

    2) 测试执行

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

    3) 测试报告

        功能自动化测试执行完成后，在Pycharm左下方Run窗口的Testing toolbar中，选择“Export Test Results”按钮即可导出测试报告

    详见[《PyCharm运行Nosetests并导出测试报告》](http://lovesoo.org/pycharm-run-nosetests-and-exports-test-report.html)

2) 性能测试

    1) 配置config/locust.yml

    2) 运行test_locust.py生成locustfile及执行性能测试，命令如下：

    ```
    $ cd Taffy\Tests
    $ python test_locust.py
    ```

    3) 测试报告

        1) 普通模式

            locust以普通模式运行时，可在[web页面](http://localhost:8089/)实时查看运行结果，包括请求数，响应时间，RPS，失败率等

            测试执行完成后可在WEB页面下载CSV格式测试报告（选择Download Data -> Download response time distribution CSV）

        2) no-web模式

            locust以no-web模式运行时，csv格式数据会定时保存在运行目录下，如locust_distribution.csv和locust_requests.csv

    Taffy集成locust性能测试框架使用说明，详见[附录7-1](https://github.com/lovesoo/Taffy#71-locust框架集成使用说明)


## 5.参考资料

1. http://nose.readthedocs.io/en/latest/index.html

2. https://docs.python.org/dev/library/unittest.html

3. https://docs.locust.io/en/latest/

4. http://www.cnblogs.com/yufeihlf/p/5764099.html


## 6.联络方式

QQ交流群：[25452556](https://jq.qq.com/?_wv=1027&k=5pqB0UV)


## 7. 附录

### 7.1 locust框架集成使用说明
#### 7.1.1.Locust简介
Locust是使用Python语言编写实现的开源性能测试工具，简洁、轻量、高效，并发机制基于gevent协程，可以实现单机模拟生成较高的并发压力。

官网：https://locust.io/

主要特点如下：
1. 使用普通的Python脚本用户测试场景
2. 分布式和可扩展，支持成千上万的用户
3. 基于Web的用户界面，用户可以实时监控脚本运行状态
4. 几乎可以测试任何系统，除了web http接口外，还可自定义clients测试其他类型系统


#### 7.1.2. 安装
可以使用pip快速安装Locust：

```
pip install locustio
```

#### 7.1.3. 使用方法
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

### 7.2 nose编写测试用例方法

nose会自动识别源文件，目录或包中的测试用例。

任何匹配testMatch正则表达式（默认为(?:^|[\\b_\\.-])[Tt]est，在一个单词的边界处或者紧跟-或_处有test或Test）的函数或类，并且所在的模块也匹配该表达式，都会被识别为测试并执行。

出于对unittest兼容性的考虑，nose也支持继承unittest.TestCase的子类测试用例。与py.test类似，nose按照测试集在模块文件中出现的顺序执行功能测试。继承于TestCase的测试集和测试类按照字母表顺序执行。

1) Fixtures

    nose支持包，模块，类和函数例级别的Fixtures（setup和teardown方法，用以自动测试的初始化或者清理工作）

2) Test packages

    nose允许测试例以包的方式分组。

    因此，也需要包级别的setup；比如，如果你想要创建一个数据库测试，你可能会想要在包setup时创建数据库，当每个测试结束之后运行包teardown时，销毁它。而不是在每一个测试模块或者测试例中创建和销毁数据库。

    想要创建包级别的setup和teardown函数，你需要在测试包的_ init_.py 函数中定义setup和teardown函数。setup函数可以被命名为setup，setup_package，setUp，或者setUpPackage；teardown可以被命名为teardown,teardown_package, tearDown, 或者tearDownPackage。一旦第一个测试模块从测试包中被加载后，一个包中的测试例就开始执行。

3) Test modules

    Test modules是一个匹配testMatch的python模块。

    测试模块提供模块级别的setup和teardown。可以定义setup, setup_module, setUp, setUpModule用于setup，teardown, teardown_module, tearDownModule用于teardown。一旦一个模块中所有的用例被收集完后，模块中的测试就开始执行。

4) Test classes

    Test classes是模块中定义的匹配testMatch或者继承unittest.TestCase的类。

    所有的测试类以相同方式运行：通过testMatch匹配的找到类中的方法，并以全新的测试类实例运行测试方法。

    像继承于unittest.TestCase的子类一样，测试类可以定义setUp tearDown函数，它们将会分别在每一个测试方法之前和之后运行。类级别setup fixture可以被命名为setup_class, setupClass, setUpClass, setupAll, setUpAll；teardown被命名为teardown_class, teardownClass, tearDownClass, teardownAll, tearDownAll, 类级别setup和teardown必须是类方法。

5) Test functions

    模块中任何匹配TestMatch的方法都将会被FunctionTestCase装饰，然后以用例的方式运行。最简单的失败和成功的用例如下：

    ```
    def test():
        assert False
    def test():
        pass
    ```

    测试函数也可定义setup和teardown属性，它们将会在测试函数开始和结束的时候运行。还可以使用@with_setup装饰器，该方式尤其适用于在相同的模块中的许多方法需要相同的setup操作。

    ```
    def setup_func():
        "set up test fixtures"

    def teardown_func():
        "tear down test fixtures"

    @with_setup(setup_func, teardown_func)
    def test():
        "test ..."
    ```

6) Test generators

    nose支持生成器测试函数和测试方法。如下：

    ```
    def test_evens():
        for i in range(0, 5):
            yield check_even, i, i*3

    def check_even(n, nn):
        assert n % 2 == 0 or nn % 2 == 0
    ```
    上述代码执行五次测试。nose生成迭代器，创建一个函数测试用例包，包装每一个yield tuple。

    Test generators必须yield tuples,且第一个元素必须是可调用的函数，其他的元素作为参数传递。

    Test generators测试用例默认名称是函数或方法的名字+参数。如果你想要显示不同的名称，可以设置yield函数的description属性。

    Test generators中定义的setup和teardown函数仅仅会被执行一次。若想对于每一个yield的用例都执行，可将setup和teardown属性设置到被yield的函数中，或者yield一个带有setup和teardown属性的可调用对象的实例。

    比如：

    ```
    @with_setup(setup_func, teardown_func)
    def test_generator():
        # ...
        yield func, arg, arg # ...
    ```
    上面的例子中，setup和teardown只会被执行一次。与此相比：

    ```
    def test_generator():
        # ...
        yield func, arg, arg # ...

    @with_setup(setup_func, teardown_func)
    def func(arg):
        assert something_about(arg)
    ```

    这个例子中，setup和teardown函数将会在每一次yield中执行。

    对于生成器方法，class中的setUp和tearDown方法将会在每一个生成的测试用例之前或者之后运行。setUp和tearDown方法并不会在生成器方法本身 之前运行，这就导致在第一个用例运行之前setUp运行两次，之间却没有tearDown运行。

    请注意，unittest.TestCase子类不支持Test generators方法。

### 7.3 Jenkins集成taffy进行自动化测试并输出测试报告

详见：http://lovesoo.org/jenkins-integrated-taffy-for-automated-testing-and-output-test-reports.html