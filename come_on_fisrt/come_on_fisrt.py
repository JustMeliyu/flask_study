# encoding:utf-8

from flask import Flask, render_template, request, redirect, url_for, flash, session
import config
from exts import db
from models import Users, Articles, Comments, Tags, article_tag
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        # 判断用户名是否存在
        if password == '' or telephone == '':
            flash('用户名或密码不能为空', 'error')
            return render_template('login.html')
        else:
            current_user = Users.query.filter(Users.telephone == telephone).first()
        if not current_user:
            flash('该用户名不存在，请重新注册后再登录', 'error')
            return render_template('login.html')
        else:
            # 判断密码是否正确
            if current_user.password != password:
                flash('密码错误，请重新输入；', 'error')
                return render_template('login.html')
            else:
                session['telephone'] = current_user.telephone
                session['username'] = current_user.username
                return redirect(url_for('index'))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        register_user = Users.query.filter(Users.telephone == telephone).first()
        # 如果手机号以填写，则弹出提示
        if register_user:
            flash('该手机号以注册，请重新输入；', 'error')
            return render_template('register.html')
        else:
            # 两次输入的密码需保持一致
            if password1 != password2:
                flash('两次输入的密码不一致，请重新输入；', 'error')
                return render_template('register.html')
            elif password1 == '':
                flash('密码不能为空；', 'error')
                return render_template('register.html')
            else:
                register_user = Users(telephone=telephone, username=username, password=password1)
                db.session.add(register_user)
                db.session.commit()
                return redirect(url_for('login'))


@app.route('/user/<username>')
def user(username):
    if session.get('username') == username:
        return render_template('user.html')
    else:
        return redirect(url_for('login'))


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/publish/', methods=['GET', 'POST'])
def publish():
    if session.get('username'):
        if request.method == 'GET':
            return render_template('publish.html')
        else:
            article_type = 'science'
            title = request.form.get('title')
            content = request.form.get('content')
            article = Articles(type=article_type, title=title, content=content)
            author = Users.query.filter(Users.username == session['username']).first()
            article.author = author
            db.session.add(article)
            db.session.commit()
            return 'yes'
    else:
        return redirect(url_for('login'))


@app.route('/article/<article_id>')
def article(article_id):
    article = Articles.query.filter(Articles.id == article_id).first()
    if article:
        article_info = {
            'title': article.title,
            'content': article.content,
            'create_time': article.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'author': article.author.username
        }
        return render_template('article.html', article=article_info)
    else:
        return 'Not Found!'


if __name__ == '__main__':
    app.run()
