# encoding: utf-8
import os
import time
import traceback
import sys
from flask import Blueprint, request, g
from app.helpers.public import check_params_exist, jsonify, get_result, allow_cross_domain
from app.services.article import get_page_article, p_article, file_is_legal, get_excel_data, write_excel
from app.models.articles import Articles
from config import db, logger, data as c_data
article = Blueprint('article', __name__)
reload(sys)
sys.setdefaultencoding('utf-8')


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
        print(type(article_dital.create_time))
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
@check_params_exist(required=["token"])
def upload_article():
    fname = request.files.get('file')
    token = request.values.get('token')
    g.token = token
    if fname:
        is_legal_file = file_is_legal(fname.filename)
        if is_legal_file:
            t = time.strftime('%Y%m%d%H%M%S')
            file_path = os.path.join(os.getcwd(), c_data.file_path.get("upload"))
            new_fpath = file_path + t + fname.filename
            fname.save(new_fpath)  # 保存文件到指定路径
            result = get_excel_data(new_fpath)
        else:
            return jsonify(get_result('ERROR_FILE', {}))
    else:
        return jsonify(get_result("NO_FILE", {}))
    if result.get("ERROR"):
        return jsonify(get_result(result.get("ERROR"), {}))
    else:
        return jsonify(get_result("SUCCESS", result.get("DATA")))


@article.route('/download')
def download_article():
    result = write_excel()
    return jsonify(get_result("SUCCESS", result.get("DATA")))

