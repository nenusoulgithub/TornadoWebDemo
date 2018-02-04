# -*- coding: UTF-8 -*-
from tornado.web import Application
from views.index import IndexHandler
from views.index import Json1Handler
from views.index import Json2Handler
from views.index import WriteHandler
from views.index import HomeHandler
from views.index import HeaderHandler
from views.index import StatusHandler
from views.index import RedirectHandler
from views.index import ErrorHandler
from config import settings


class Application(Application):
    def __init__(self):
        handlers = [
            ("/", IndexHandler),
            ("/home", HomeHandler),
            (r"/write", WriteHandler),
            (r"/json1", Json1Handler),
            (r"/json2", Json2Handler),
            (r"/header", HeaderHandler),
            (r"/status", StatusHandler),
            (r"/redirect", RedirectHandler),
            (r"/error", ErrorHandler),
        ]

        super(Application, self).__init__(handlers=handlers, **settings)
