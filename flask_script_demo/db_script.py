# encoding:utf-8

from flask_script import Manager
from flask_script_demo import app

DBManager = Manager(app)


@DBManager.command
def init():
    print '初始化完成！'


@DBManager.command
def migrate():
    print '数据库迁移成功！'
