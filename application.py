# -*- coding: UTF-8 -*-
from tornado.web import Application
from views.index import IndexHandler
from views.index import HomeHandler
from config import settings


class Application(Application):
    def __init__(self):
        handlers = [
            ("/", IndexHandler),
            ("/home", HomeHandler)
        ]

        super(Application, self).__init__(handlers=handlers, **settings)
