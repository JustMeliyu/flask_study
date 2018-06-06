from config import *
from initializer import app, db
from view import *

app.register_blueprint(index)
app.register_blueprint(publish, url_prefix='/test')
app.register_blueprint(auth)
app.register_blueprint(article, url_prefix='/cate')
app.register_blueprint(comment)
app.register_blueprint(not_found)
app.register_blueprint(user)
app.register_blueprint(register)
app.register_blueprint(t_json)
