# encoding:utf-8

from flask import render_template, Blueprint, request
from app.models.articles import Articles
from config import db, data
from app.helpers.tool import class_to_dict
from app.services.index import RegistForm

index = Blueprint('index', __name__)


@index.route('/')
def index_page():
    all_articles = []
    # 显示最新三篇文章
    articles = Articles.query.order_by(db.desc(Articles.create_time))
    articles = articles.all()
    if articles:
        article_num = (len(articles) if data.index_article_num >= len(articles) else data.index_article_num)
        for i in range(article_num):
            author = articles[i].author.username
            articles[i] = class_to_dict(articles[i])
            articles[i]['author'] = author
            articles[i]['content'] = articles[i]['content'][0:40] + '......'
            all_articles.append(articles[i])
    return render_template('index.html', articles=all_articles)


@index.route('/gogo/', methods=['GET', 'POST'])
def flask_wtf():
    if request.method == 'GET':
        return render_template('flask_wtf.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            print username, password
            return u'登录成功'
        else:
            print form.errors
            return u'参数错误'
