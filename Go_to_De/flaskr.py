# all the imports

import os
import sqlite3
from flask import Flask
app = Flask(__name__)


print app.root_path
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route('/')
def connect_db():
    # Connects to the specific database.
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    with app.app_context():
        db = connect_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescriot(f.read())
        db.commit()


if __name__ == '__main__':
    app.run()
