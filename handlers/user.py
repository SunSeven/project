#!../venv/bin/python
# encoding: utf-8

from __future__ import absolute_import
import tornado.escape
import tornado.web
from methods.readdb import select_table
from .base import BaseHandler

class UserHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # print("begin")
        # username = self.get_argument("user")
        username = tornado.escape.json_decode(self.current_user)
        # name = self.get_secure_cookie(username)
        # print("name = ", name)
        # print("user = ", username)
        user_infos = select_table(table="user", column="*", condition="name", value=username)
        # print("user_infos = ", user_infos)
        self.render("user.html", users = user_infos)

