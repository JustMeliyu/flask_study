
# -*- coding:utf-8 -*-


import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from giraffe import Config, Logger
import data as c_data
from flask_sso import SSO


_current_path = os.path.dirname(__file__)

# load configurations
config = Config(
    # load yaml files, put file name into the list, e.g. we put "mysql" for
    # file "mysql.yml".
    yamls=["app", "mysql", "redis"],

    # project config path, will load config files under this path.
    config_path=_current_path
)

# prepare logger
logger = Logger.create(
    # project log path, will print log file under this path.
    log_path=os.path.join(_current_path, "..", "log"),

    # application name
    app_name="come_on_first",

    # environment stage, could be DEVELOPMENT, TEST, STAGING, PRODUCTION
    stage=config["STAGE"]
)

# initialize application instances
app = Flask(__name__)
# app for template
# app = Flask(__name__, static_folder="../app/static", template_folder="../app/templates")
print "======"
print type(app.config)
for c in app.config:
    print c
print "======"

print "app.config is : %s " % app.config
# app.config.from_object(c_data)
app.config['SQLALCHEMY_DATABASE_URI'] = config["MYSQL_DATABASE_URI"]
print 'SQLALCHEMY_DATABASE_URI is : %s' % app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config["APP_TRACK_MODIFICATIONS"]
app.config['SQLALCHEMY_ECHO'] = config["APP_ECHO"]
app.config['SSO_ATTRIBUTE_MAP'] = c_data.SSO_ATTRIBUTE_MAP
db = SQLAlchemy(app)
ext = SSO(app=app)

# @sso.login_handler
# def login_callback(user_info):
#     """Store information in session."""
#     session['user'] = user_info
# end
