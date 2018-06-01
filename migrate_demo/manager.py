# encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from exts import db
from migrate_demo import app
from models import Article


# 数据路迁移步骤
# init               migrate                 upgrade
# 模型(修改)   ->    迁移文件(生成)    ->    表(映射)
manager = Manager(app)
# 要使用flask_migrate，必须绑定app和db
migrate = Migrate(app, db)
# 把migratecommand命令添加到manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
