# -*- coding:utf-8 -*-


from .initializer import app, db, logger, config
from .routes import register_routes
from .data import *

register_routes(app)
