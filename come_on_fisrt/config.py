# encoding:utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

# dialect+driver://username:password@host:port/database

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = 'Admin.2@cd'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo2'


# SQLALCHEMY会在 config文件读取一个名为 SQLALCHEMY_DATABASE_URI 的字符串，然后把该字符串放入SQLALCHEMY中，进行数据库的连接
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
