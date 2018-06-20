# encoding:utf-8
import os
# DEBUG = True

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
    "LACK_PARAM": 1003,
    "EXIST_USER": 1004,
    "PWD_DIFF": 1005,
    "PARAM_EMPTY": 1006,
    "TOKEN_EXPIRE": 1007,
    "PARAM_ERROR": 1008,
    "NO_FILE": 1009,
    "ERROR_FILE": 1010,
    "ERROR_FILE_CONTENT": 1011,
    "AUTHOR_NOT_EXIST": 1012
}

errmsg = {
    "SUCCESS": u"成功",
    "DB_ERROR": u"数据库错误",
    "WRONG_PASSWORD": u"用户名或密码错误",
    "LACK_PARAM": u"缺少必要参数",
    "EXIST_USER": u"已存在用户",
    "PWD_DIFF": u"密码不一致",
    "PARAM_EMPTY": u"参数为空",
    "TOKEN_EXPIRE": u"token过期",
    "PARAM_ERROR": u"参数错误",
    "NO_FILE": u"请上传文件",
    "ERROR_FILE": u"错误文件",
    "ERROR_FILE_CONTENT": u"错误文件内容",
    "AUTHOR_NOT_EXIST": u"作者不存在"
}

article_key = ["author", "title", "type", "content", "create_time"]

article_type = ["movie", "game", "sport", "science", "other"]

file_legality = ['xlsm', 'xlsx']

start_row = 3
start_col = 2
end_col = 5
