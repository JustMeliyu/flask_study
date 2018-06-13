# encoding: utf-8

from flask import Blueprint, request
from models import Users
from exts import db
from helpers.tools import *
import hashlib
from config import config, logger
register = Blueprint('register', __name__)


@register.route('/register/', methods=['POST'])
def register_user():
    try:
        telephone = request.form.get('telephone').strip()
        username = request.form.get('username').strip()
        password1 = request.form.get('password1').strip()
        password2 = request.form.get('password2').strip()
    except:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        logger.info(u"缺少关键参数")

    user_telephone = Users.query.filter(Users.telephone == telephone).first()
    # 如果手机号以填写，则弹出提示
    if not telephone or not username or not password1 or not password2:
        return jsonify(get_result("LACK_PARAMETER", {}))
    elif user_telephone:
        return jsonify(get_result("EXIST_USER", {}))
    elif password2 != password1:
        return jsonify(get_result("PWD_DIFF", {}))
    else:
        password = hashlib.md5(password1)
        reg_user = Users(telephone=telephone, username=username, password=password.hexdigest())
        db.session.add(reg_user)
        db.session.commit()
        data = {
            "id": reg_user.id,
            "username": reg_user.username,
            "telephone": reg_user.telephone,
            "create_time": reg_user.create_time
        }
        return jsonify(get_result("SUCCESS", data))
