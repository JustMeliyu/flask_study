# encoding:utf-8

from flask import render_template, Blueprint
from models import Articles
from exts import db
import config
from services.public import class_to_dict

index = Blueprint('index', __name__)


@index.route('/')
def index_page():
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