# encoding: utf-8
from flask import Flask, session, render_template, request, g, redirect, url_for
import os
from datetime import timedelta
from utils import login_log, login_failed
app = Flask(__name__)
# 添加数据到session中，操作session与操作字典相同
# SECRET_KEY
app.config['SECRET_KEY'] = os.urandom(24)
app.config['TESTING'] = True
# 通过该参数设置session过期时间
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)


@app.route('/')
def hello_world():
    session['username'] = 'ly'
    # 设置为session.permanent = True，有效期为31天
    session.permanent = True
    return 'Hello World!'


@app.route('/get/')
def get():
    print session.get('username')
    print request.args.get('q')
    return render_template('get.html')


@app.route('/delete/')
def delete():
    print session.get('username')
    session.pop('username')
    print session.get('username')
    return 'success'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:

        g.username = request.form.get('username')
        g.password = request.form.get('password')
        if g.username == 'ly' and g.password == '111':
            login_log()
            return 'login success'
        else:
            login_failed()
            return 'login failed'


@app.route('/login_g', methods=['GET', 'POST'])
def login_g():
    return render_template('login_g.html')


@app.before_request
def get_info():
    print 'before_request is work'


@app.context_processor
def get_context():
    return {'username': 1111}

if __name__ == '__main__':
    app.run(debug=True)
