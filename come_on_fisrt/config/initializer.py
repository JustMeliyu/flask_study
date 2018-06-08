import os
import config as local_config
# from config import SQLALCHEMY_TRACK_MODIFICATIONS
from exts import db
from flask import Flask
from giraffe import Config, Logger

_current_path = os.path.dirname(__file__)
config = Config(
    config_path=_current_path,
    yamls=['mysql']
)

logger = Logger.create(
    log_path=os.path.join(_current_path, "..", "log"),
    app_name="come_on_first",
    stage=config.config["STAGE"]
)


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['SQLALCHEMY_DATABASE_URI'] = config.config["MYSQL_DATABASE_URI"]
logger.info(app.config['SQLALCHEMY_DATABASE_URI'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(local_config)
db.init_app(app)
