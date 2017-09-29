# coding:utf-8
import yaml
import os
import codecs


class locustUtil(object):
    def __init__(self, locustyml='config/locust.yml'):
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
        locustyml_path = os.path.join(project_path, locustyml)
        self.cases = yaml.load(file(locustyml_path, 'r'))

    def getRunCommand(self):
        '''
        从locust.yml配置文件，获取locust运行命令
        '''
        mode = self.cases.get('mode', 0)
        if mode:
            csv = self.cases.get('csv', 'locust')
            c = self.cases.get('c', 10)
            r = self.cases.get('r', 2)
            run_time = self.cases.get('run_time', '5m')
            return '--no-web --csv={0} -c{1} -r{2} --run-time {3}'.format(csv, c, r, run_time)
        else:
            return None

    def genLocustfile(self, name='locustfile.py'):
        """
        使用locust.yml配置文件及template/下模板，生成性能测试脚本
        """
        # 获取最大，最小等待时间
        min_wait = str(self.cases.get('min_wait', 100))
        max_wait = str(self.cases.get('max_wait', 1000))
        tasks = self.cases['task']
        res = []
        # 先对tasks中clas+function进行去重处理
        tasks = dict((i["class"] + i["function"], i) for i in tasks).values()

        # 依次生成import,func,task
        for task in tasks:
            # 定义临时dict
            tmp = {}

            # 获取task详细配置
            file_name = task.get('file').strip('.py').replace('/','.').replace('\\','.')
            class_name = task.get('class')
            function_name = task.get('function')
            weight = str(task.get('weight', 1))

            with codecs.open(os.path.join(os.path.dirname(__file__), 'template/import_template'), encoding='utf-8') as import_template:
                import_content = import_template.read()
                import_content = import_content.replace('$file', file_name)
                import_content = import_content.replace('$class', class_name)
                tmp['import'] = import_content

            with codecs.open(os.path.join(os.path.dirname(__file__), 'template/function_template'), encoding='utf-8') as function_template:
                function_content = function_template.read()
                function_content = function_content.replace('$class', class_name)
                function_content = function_content.replace('$function', function_name)
                tmp['function'] = function_content

            with codecs.open(os.path.join(os.path.dirname(__file__), 'template/task_template'), encoding='utf-8') as task_template:
                task_content = task_template.read()
                task_content = task_content.replace('$weight', weight)
                task_content = task_content.replace('$class', class_name)
                task_content = task_content.replace('$function', function_name)
                tmp['task'] = task_content

            res.append(tmp)

        # 生成完整的import,function,task内容
        import_content = '\r\n'.join(set([i['import'] for i in res]))
        function_content = '\r\n\r\n'.join(set([i['function'] for i in res]))
        task_content = '\r\n\r\n'.join(set([i['task'] for i in res]))

        with codecs.open(os.path.join(os.path.dirname(__file__), 'template/locustfile_template'), encoding='utf-8') as locustfile_template:
            with codecs.open(name, mode='w', encoding='utf-8') as f:
                locustfile_content = locustfile_template.read()
                locustfile_content = locustfile_content.replace('$import', import_content)
                locustfile_content = locustfile_content.replace('$function', function_content)
                locustfile_content = locustfile_content.replace('$min_wait', min_wait)
                locustfile_content = locustfile_content.replace('$max_wait', max_wait)
                locustfile_content = locustfile_content.replace('$task', task_content)
                f.write(locustfile_content)

        return name
