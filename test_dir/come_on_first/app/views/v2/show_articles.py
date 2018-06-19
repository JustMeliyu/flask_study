# encoding:utf-8

import sys
from flask import Blueprint, request
from app.models.articles import Articles
from config import db
from app.helpers.tool import class_to_dict, jsonify, get_result
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')
show_articles = Blueprint('show_articles', __name__)


@show_articles.route('')
def get_articles():

    condition = request.values.get("condition", None)
    sort = request.values.get("sort", None)
    page_index = int(request.values.get("page_index", 1))
    page_size = int(request.values.get("page_size", 10))
    query_result = Articles.query
    data = []
    try:
        if condition:
            query_result = query_result.filter(Articles.title.like('%{}%'.format(condition)) |
                                               Articles.content.like('%{}%'.format(condition)) |
                                               Articles.type.like('%{}%'.format(condition)))
        if sort:
            pass
        else:
            query_result = query_result.order_by(db.desc(Articles.create_time))

        paginate = query_result.paginate(page_index, page_size)
        data = {
            'total': paginate.total,
            'data': [class_to_dict(item) for item in paginate.items]
        }
        results = jsonify(get_result('SUCCESS', data))
    except:
        print traceback.format_exc()
        results = jsonify(get_result('DB_ERROR', data))

    return results
