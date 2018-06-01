# encoding: utf-8
from flask import g


def login_log():
    print g.username


def login_failed():
    print u"用户名 %s 错误" % g.username
