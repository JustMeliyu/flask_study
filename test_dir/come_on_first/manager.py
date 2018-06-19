# encoding:utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import app, db
from app.models.articles import Articles
from app.models.users import Users
from app.models.comments import Comments


manager = Manager(app)
# 使用migrate绑定app与db
migrate = Migrate(app, db)
# 添加迁移命令到manager中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
