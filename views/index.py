# -*- coding: UTF-8 -*-
from tornado.web import RequestHandler


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
