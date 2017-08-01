#!../venv/bin/python
# encoding: utf-8

import MySQLdb

conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="test")

cur = conn.cursor()
