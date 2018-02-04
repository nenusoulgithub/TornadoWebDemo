# -*- coding: UTF-8 -*-
from tornado.web import RequestHandler
import json


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("guohua is a good man!\n")

    def data_received(self, chunk):
        pass


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("guohua is a good man!\n")

    def data_received(self, chunk):
        pass


class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("guohua is a good man!\n")
        self.write("guohua is a nice man!\n")
        self.write("guohua is a handsome man!\n")
        # 刷新缓冲区，关闭当次请求通道
        # 在finish下边不要再write
        self.finish()
        # self.write("guohua is a cool man!\n")

    def data_received(self, chunk):
        pass


class Json1Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "guohua",
            "age": 18,
            "height": 175,
            "weight": 175,
        }
        json_str = json.dumps(per)
        # 自定义Response Header信息
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json_str)

    def data_received(self, chunk):
        pass


class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "guohua",
            "age": 18,
            "height": 175,
            "weight": 175,
        }
        self.write(per)

    def data_received(self, chunk):
        pass


class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Context-Type", "text/html; charset=UTF-8")
        self.set_header("Guo-Hua", "nice")

    def get(self, *args, **kwargs):
        self.set_header("Guo-Hua", "good")
        self.write("guohua is a good man!\n")

    def data_received(self, chunk):
        pass


class StatusHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        # 反正正常状态码，不需要携带reason
        # self.set_status(404)
        # 返回非正常状态码，需要携带reason
        # self.set_status(999, "what is status code?")
        # 返回非正常状态码，并且不携带reason
        self.set_status(999)
        self.write("guohua is a good man!\n")


class RedirectHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
        self.redirect("/")


class ErrorHandler(RequestHandler):
    def data_received(self, chunk):
        pass

    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            self.write("服务器内部错误！\n")
        elif status_code == 404:
            self.write("资源丢失！\n")

        # self.set_status(status_code)

    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag == "500":
            self.send_error(500)
        elif flag == "404":
            self.send_error(404)
        self.write("guohua is a good man!\n")
