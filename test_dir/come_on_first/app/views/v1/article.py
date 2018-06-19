# encoding: utf-8
import os
import time
import traceback
import xlrd
from flask import Blueprint, request, g
from app.helpers.public import check_params_exist, jsonify, get_result, allow_cross_domain
from app.services.article import get_page_article, p_article, file_is_legal
from app.models.articles import Articles
from config import db, logger
article = Blueprint('article', __name__)


# 获取文章信息
@article.route('')
@allow_cross_domain
@check_params_exist()
def get_article():
    page_size = int(request.values.get('page_size', 10))
    page_index = int(request.values.get('page_index', 1))
    sort = request.values.get('sort')
    title = request.values.get('title')
    content = request.values.get('content')
    article_type = request.values.get('type')
    # 按条件查询文章
    result = get_page_article(page_index, page_size, sort, title, content, article_type)
    if result.get("ERROR"):
        return jsonify(get_result(result.get("ERROR"), {}))
    else:
        return jsonify(get_result("SUCCESS", result.get("DATA")))


# 获取文章详细信息
@article.route('/<article_id>')
@allow_cross_domain
def article_info(article_id):
    try:
        article_dital = Articles.query.filter_by(id=article_id).first()
        data = {
            "title": article_dital.title,
            "content": article_dital.content,
            "type": article_dital.type,
            "create_time": article_dital.create_time,
            "author": article_dital.author.username
        }
        return jsonify(get_result("SUCCESS", data))
    except:
        db.session.rollback()
        logger.info(traceback.format_exc())
        return jsonify(get_result("DB_ERROR", {}))


# 发布文章
@article.route('/publish', methods=['POST'])
@allow_cross_domain
@check_params_exist(required=["title", "content", "type", "token"])
def publish_article():
    title = request.values.get("title").strip()
    content = request.values.get("content").strip()
    article_type = request.values.get("type").strip()
    token = request.values.get("token").strip()

    # 发布文章信息
    g.token = token
    result = p_article(title, content, article_type)
    if result.get("ERROR"):
        return jsonify(get_result(result.get("ERROR"), {}))
    else:
        return jsonify(get_result("SUCCESS", result.get("DATA")))


# 上传文章
@article.route('/upload', methods=['POST'])
def upload_article():
    fname = request.files.get('file')
    if fname:
        is_legal_file = file_is_legal(fname)
        if is_legal_file:
            pass
        else:
            return jsonify(get_result('ERROR_FILE', {}))
        t = time.strftime('%Y%m%d%H%M%S')
        file_path = os.path.join(os.getcwd(), "file/")
        print(file_path)
        new_fname = file_path + t + fname.filename
        print(new_fname)
        fname.save(new_fname)  # 保存文件到指定路径
        return '{"code": "ok"}'
    else:
        return jsonify(get_result("NO_FILE", {}))
