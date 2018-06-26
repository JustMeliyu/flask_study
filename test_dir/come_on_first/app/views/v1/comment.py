# encoding: utf-8

from flask import Blueprint, g, request
from app.helpers.public import jsonify, get_result, check_params_exist, allow_cross_domain
from app.services.comment import get_page_comment, p_comment
comment = Blueprint("comment", __name__)


@comment.route("")
@allow_cross_domain
@check_params_exist(required=["page_size", "page_index", "article_id"])
def get_comment():
    page_size = int(request.values.get('page_size', 10))
    page_index = int(request.values.get('page_index', 1))
    article_id = request.values.get("article_id")
    # 按条件查询文章
    result = get_page_comment(page_index, page_size, article_id)
    if result.get("ERROR"):
        return jsonify(get_result(result.get("ERROR"), {}))
    return jsonify(get_result("SUCCESS", result.get("DATA")))


@comment.route("/publish", methods=["POST"])
@allow_cross_domain
@check_params_exist(required=["content", "article_id", "token"])
def publish_comment():
    content = request.values.get("content").strip()
    article_id = request.values.get("article_id").strip()
    token = request.values.get("token").strip()

    # 发布评论信息
    g.token = token
    result = p_comment(content, article_id)
    if result.get("ERROR"):
        return jsonify(get_result(result.get("ERROR"), {}))
    return jsonify(get_result("SUCCESS", result.get("DATA")))
