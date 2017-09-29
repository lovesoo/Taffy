import time
from locust import Locust, TaskSet, events, task
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from test_demo import test_demo


class HttpClient(object):
    def __init__(self):
        pass

    def test_demo_test_webservice(self):
        start_time = time.time()
        try:
            test_demo().test_webservice()
            request_type = test_demo.__name__
            name = test_demo().test_webservice.__name__
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=request_type, name=name, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type=request_type, name=name, response_time=total_time, response_length=0)

    def test_demo_test_httpbin_get(self):
        start_time = time.time()
        try:
            test_demo().test_httpbin_get()
            request_type = test_demo.__name__
            name = test_demo().test_httpbin_get.__name__
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=request_type, name=name, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type=request_type, name=name, response_time=total_time, response_length=0)

    def test_demo_test_httpbin_post(self):
        start_time = time.time()
        try:
            test_demo().test_httpbin_post()
            request_type = test_demo.__name__
            name = test_demo().test_httpbin_post.__name__
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type=request_type, name=name, response_time=total_time, exception=e)
        else:
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type=request_type, name=name, response_time=total_time, response_length=0)


class HttpLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(HttpLocust, self).__init__(*args, **kwargs)
        self.client = HttpClient()


class ApiUser(HttpLocust):
    min_wait = 100
    max_wait = 1000

    class task_set(TaskSet):
        @task(1)
        def test_demo_test_webservice(self):
            self.client.test_demo_test_webservice()

        @task(1)
        def test_demo_test_httpbin_post(self):
            self.client.test_demo_test_httpbin_post()

        @task(2)
        def test_demo_test_httpbin_get(self):
            self.client.test_demo_test_httpbin_get()
