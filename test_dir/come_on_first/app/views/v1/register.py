# encoding: utf-8

from flask import Blueprint, request
from app.helpers.tool import jsonify, get_result
import hashlib
from config import db
from app.models.users import Users
from app.helpers.public import check_params_exist
register = Blueprint('register', __name__)


# 注册用户
@register.route('', methods=['POST'])
@check_params_exist(required=["telephone", "username", "password1", "password2"])
def register_user():
    telephone = request.form.get('telephone').strip()
    username = request.form.get('username').strip()
    password1 = request.form.get('password1').strip()
    password2 = request.form.get('password2').strip()

    user = Users.query.filter(Users.telephone == telephone).first()
    # 如果手机号以填写，则弹出提示
    if user:
        return jsonify(get_result("EXIST_USER", {}))
    elif password2 != password1:
        return jsonify(get_result("PWD_DIFF", {}))
    else:
        password = hashlib.md5(password1)
        reg_user = Users(telephone, username, password.hexdigest())
        db.session.add(reg_user)
        db.session.commit()
        data = {
            "id": reg_user.id,
            "username": reg_user.username,
            "telephone": reg_user.telephone,
            "create_time": reg_user.create_time
        }
        return jsonify(get_result("SUCCESS", data))
