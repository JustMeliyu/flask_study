# encoding: utf-8

from flask import request, Blueprint, g
from app.helpers.tool import jsonify, get_result
from app.helpers.public import check_params_exist, allow_cross_domain
from uuid import uuid1
import hashlib
from app.services.login import get_user
auth = Blueprint('auth', __name__)


# 登录
@auth.route('', methods=['POST'])
@allow_cross_domain
@check_params_exist(required=['telephone', 'password'])
def login():
    telephone = request.values.get('telephone')
    password = request.values.get('password')
    m2 = hashlib.md5(password)
    token = uuid1()
    g.token = token
    result = get_user(telephone, m2.hexdigest())
    if result.get("ERROR"):
        return jsonify(get_result(result.get("ERROR"), {}))
    else:
        return jsonify(get_result("SUCCESS", dict({"token": token}, **result.get("DATA"))))

