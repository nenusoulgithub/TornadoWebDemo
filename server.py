#!/usr/bin/python
# -*- coding: UTF-8 -*-
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from config import options
from application import Application


if __name__ == '__main__':
    app = Application()

    httpServer = HTTPServer(app)
    httpServer.bind(options["port"])
    httpServer.start(1)

    IOLoop.current().start()
