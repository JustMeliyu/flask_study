# encoding:utf-8
import os
DEBUG = True

SECRET_KEY = os.urandom(24)

# dialect+driver://username:password@host:port/database

# DIALECT = 'mysql'
# DRIVER = 'mysqldb'
# USERNAME = 'root'
# PASSWORD = 'Admin.2@cd'
# HOST = '127.0.0.1'
# PORT = '3306'
# DATABASE = 'come_on_first'
#
#
# # SQLALCHEMY会在 config文件读取一个名为 SQLALCHEMY_DATABASE_URI 的字符串，然后把该字符串放入SQLALCHEMY中，进行数据库的连接
# SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False

index_article_num = 3

errcode = {
    "SUCCESS": 1000,
    "DB_ERROR": 1001,
    "WRONG_PASSWORD": 1002,
    "LACK_PARAMETER": 1003,
    "EXIST_USER": 1004,
    "PWD_DIFF": 1005
}

errmsg = {
    "SUCCESS": u"成功",
    "DB_ERROR": u"数据库错误",
    "WRONG_PASSWORD": u"用户名或密码错误",
    "LACK_PARAMETER": u"缺少必要参数",
    "EXIST_USER": u"已存在用户",
    "PWD_DIFF": u"密码不一致"
}
