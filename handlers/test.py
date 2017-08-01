#!../venv/bin/python
# encoding: utf-8

import tornado.web
import tornado.gen
import time

"""
class SleepHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 17, callback=self.on_response)
   
    def on_response(self):    
        self.write("sleepHandler")
        self.finish()
"""

class SleepHandler(tornado.web.RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        #yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 17)
        yield tornado.gen.sleep(17)
        self.write("sleepHandler")

class SeeHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("seeHandler")
