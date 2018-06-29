# encoding: utf-8
from flask import g
from app.models.comments import Comments
from app.models.articles import Articles
from app.helpers.public import class_to_dict
from app.helpers.build_redis import is_login
import traceback
from config import logger, db


def get_page_comment(page_index, page_size, article_id):
    q = Articles.query.filter_by(article_id=article_id).first()
    cs = g.comments.paginate(page_index, page_size)
    try:
        query_result = Comments.query.filter_by(article_id=article_id).paginate(page_index, page_size)
        data = {
            "total": query_result.total,
            "data": [class_to_dict(item) for item in query_result.items]
        }
        return {"DATA": data}
    except:
        logger.info(traceback.format_exc())
        return {"ERROR": "DB_ERROR"}


@is_login
def p_comment(content, article_id):
    try:
        if len(content) > 140:
            return {"ERROR": "PARAM_ERROR"}
        comment = Comments.new(content, article_id, g.current_user_id)
        data = {
            "content": content,
            "article_id": article_id,
            "user_id": g.current_user_id,
            "publish_user": comment.author.username,
            "create_time": comment.create_time
        }
        return {"DATA": data}
    except:
        db.session.rollback()
        logger.info(traceback.format_exc())
        return {"ERROR": "DB_ERROR"}
