# encoding: utf-8

import xlrd
from app.models.articles import Articles
from app.helpers.public import class_to_dict
from app.helpers.build_redis import is_login
import traceback
from config import logger, db, data as c_data
# from config import data as c_data
from flask import g


def get_page_article(page_index, page_size, sort, title, content, article_type):
    try:
        query_result = Articles.query
        if sort:
            query_result = query_result.order_by(db.desc(Articles.create_time))
        if title:
            query_result = query_result.filter(Articles.title.like('%{}%'.format(title)))
        if content:
            query_result = query_result.filter(Articles.content.like('%{}%'.format(content)))
        if article_type:
            query_result = query_result.filter(Articles.type.like('%{}%'.format(article_type)))
        paginate = query_result.paginate(page_index, page_size, False)
        data = {
            "total": len(paginate.items),
            "data": [class_to_dict(item) for item in paginate.items]
        }
        return {"DATA": data}
    except:
        db.session.rollback()
        logger.info(traceback.extract_stack())
        return {"ERROR": "DB_ERROR"}


@is_login
def p_article(title, content, article_type):
    if article_type not in c_data.article_type:
        return {"ERROR": "PARAM_ERROR"}
    if len(title) > 30:
        return {"ERROR": "PARAM_ERROR"}
    try:
        article = Articles(title=title, content=content, type=article_type, author_id=g.current_user_id)
        db.session.add(article)
        db.session.commit()
        data = {
            "id": article.id,
            "title": title,
            "content": content,
            "type": article_type,
            "author_id": g.current_user_id,
            "create_time": article.create_time
        }
        return {"DATA": data}
    except:
        db.session.rollback()
        logger.debug(traceback.format_exc())
        return {"ERROR": "DB_ERROR"}


def file_is_legal(filename):
    return '.' in filename and filename.resplit('.', 1)[1] in c_data.file_legality


def get_excel_data(filename):
    excel_file = xlrd.open_workbook(filename)




