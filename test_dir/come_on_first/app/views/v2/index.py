# encoding:utf-8

from flask import render_template, Blueprint
from app.models.articles import Articles
from config import db, data
from app.helpers.tool import class_to_dict

index = Blueprint('index', __name__)


@index.route('')
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
