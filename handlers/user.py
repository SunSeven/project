#!../venv/bin/python
# encoding: utf-8

import tornado.web
from methods.readdb import select_table

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        # print("begin")
        username = self.get_argument("user")
        name = self.get_secure_cookie(username)
        print("name = ", name)
        # print("user = ", username)
        user_infos = select_table(table="user", column="*", condition="name", value=username)
        # print("user_infos = ", user_infos)
        self.render("user.html", users = user_infos)

