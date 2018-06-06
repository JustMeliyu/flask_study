# encoding:utf-8

from flask import render_template, Blueprint
from sqlalchemy import text
from models import Articles
from exts import db
import config
from services.public import class_to_dict

index = Blueprint('index', __name__)


@index.route('/')
def index_page():
    all_articles = []
    # 显示最新三篇文章
    # t_art = Articles.query.filter_by(title=u'怦然心动')
    # t_art2 = Articles.query.filter(Articles.title == u'怦然心动')
    # print t_art
    # print t_art2
    # order_sql = " CONVERT( articles.content USING gbk ) COLLATE gbk_chinese_ci ASC "
    # t_art3 = Articles.query.order_by(text(order_sql))
    # for t in t_art3:
    #     print t.id
    #     t = class_to_dict(t)
    #     print t
    # print '======='
    # print t_art3
    # t_art4 = Articles.query.paginate(1, 10, False)
    # for t in t_art4.items:
    #     t = class_to_dict(t)
    #     print t
    # print [class_to_dict(item) for item in t_art4.items]
    articles = Articles.query.order_by(db.desc(Articles.create_time))
    articles = articles.all()
    for i in range(config.index_article_num):
        author = articles[i].author.username
        articles[i] = class_to_dict(articles[i])
        articles[i]['author'] = author
        articles[i]['content'] = articles[i]['content'][0:40] + '......'
        all_articles.append(articles[i])
    return render_template('index.html', articles=all_articles)
