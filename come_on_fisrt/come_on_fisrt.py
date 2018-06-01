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
    all_articles = []
    # 显示最新三篇文章
    articles = Articles.query.order_by(db.desc(Articles.create_time))
    articles = articles.all()
    for i in range(config.index_article_num):
        author = articles[i].author.username
        articles[i] = class_to_dict(articles[i])
        articles[i]['author'] = author
        articles[i]['content'] = articles[i]['content'][0:40] + '......'
        all_articles.append(articles[i])
    return render_template('index.html', articles=all_articles)


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
            return redirect(url_for('article', article_id=article.id))
    else:
        return redirect(url_for('login'))


@app.route('/article/<article_id>', methods=['GET', 'POST'])
def article(article_id):
    all_comments = []
    current_article = Articles.query.filter(Articles.id == article_id).first()
    if current_article:
        # 显示文章
        current_article.create_time = current_article.create_time.strftime('%Y-%m-%d %H:%M:%S')
        article_info = class_to_dict(current_article)
        article_info['author'] = current_article.author.username
        print article_info.get('author')
        # 显示评论
        comments = Comments.query.filter(Comments.article_id == article_id).all()
        for c in comments:
            author = c.author.username
            c = class_to_dict(c)
            c['author'] = author
            all_comments.append(c)
        return render_template('article.html', article=article_info, comments=all_comments)
    else:
        return redirect(url_for('not_found'))


@app.route('/article/')
def all_articles():
    all_articles = []
    # 显示所有文章
    articles = Articles.query.all()
    for article in articles:
        author = article.author.username
        article = class_to_dict(article)
        article['author'] = author
        article['content'] = article['content'][0:40] + '......'
        all_articles.append(article)
    return render_template('all_article.html', articles=all_articles)


@app.route('/comment/', methods=['POST'])
def comment():
    print session.get('username')
    article_id = request.form.get('article_id')
    comment_content = request.form.get('comment')
    if session.get('username'):
        if comment_content:
            comment = Comments(content=comment_content)
            comment.article = Articles.query.filter(Articles.id == article_id).first()
            comment.author = Users.query.filter(Users.username == session.get('username')).first()
            db.session.add(comment)
            db.session.commit()
    return redirect(url_for('article', article_id=article_id))


@app.route('/404/')
def not_found():
    return render_template('404.html')


def class_to_dict(obj):
    dict = {}
    dict.update(obj.__dict__)
    return dict


if __name__ == '__main__':
    app.run()
