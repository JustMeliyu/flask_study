# encoding:utf-8

from flask import Flask
from config import config
from exts import db
from view import *
import sys
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


app.register_blueprint(index)
app.register_blueprint(publish)
app.register_blueprint(auth)
app.register_blueprint(article)
app.register_blueprint(comment)
app.register_blueprint(not_found)
app.register_blueprint(user)
app.register_blueprint(register)

if __name__ == '__main__':
    print sys.path
    app.run()
