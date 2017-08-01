#!venv/bin/python
# encoding: utf-8

"""
the url structure of website
"""

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.test import SleepHandler, SeeHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler),
    (r'/sleep', SleepHandler),
    (r'/see', SeeHandler),
]
