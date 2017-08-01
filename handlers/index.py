#!../venv/bin/python
# encoding: utf-8

import tornado.web
from methods.readdb import select_table, select_columns

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        usernames = select_columns(table='user', column="name")
        one_user = usernames[0][0]
        self.render('index.html', user = one_user)
    
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        user_infos = select_table(table="user", column="*", condition="name", value=username)
        if user_infos:
            db_pwd = user_infos[0][1]
            if db_pwd == password:
                self.set_secure_cookie(username, password, httponly=True, secure=True)
                self.write(username)
            else:
                self.write("your password was not right.")
        else:
            self.write("There is no thi user.")
