from flask import Flask
from exts import db
import config


app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_object(config)
db.init_app(app)


