# encoding: utf-8

from flask import Blueprint, request
from app.helpers.tool import *
import traceback
from config import logger, db
from app.models.articles import Articles
article = Blueprint('article', __name__)


@article.route('/article/')
def get_article():
    page_size = int(request.values.get('page_size', 10))
    page_index = int(request.values.get('page_index', 1))
    sort = request.values.get('sort')
    title = request.values.get('title')
    content = request.values.get('content')
    article_type = request.values.get('type')
    try:
        query_article = Articles.query
        if sort:
            query_article = query_article.order_by(db.desc(Articles.create_time))
        if title:
            query_article = query_article.filter(Articles.title.like('%{}%'.format(title)))
        if content:
            query_article = query_article.filter(Articles.content.like('%{}%'.format(content)))
        if article_type:
            query_article = query_article.filter(Articles.type.like('%{}%'.format(article_type)))
        paginate = query_article.paginate(page_index, page_size, False)
        data = {
            "total": len(paginate.items),
            "data": [class_to_dict(item) for item in paginate.items]
        }
        return jsonify(get_result("SUCCESS", data))
    except:
        db.session.rollback()
        logger.info(traceback.extract_stack())
        return jsonify(get_result("DB_ERROR", {}))
