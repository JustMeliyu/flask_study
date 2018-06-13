# encoding: utf-8

from flask import request, Blueprint
from app.helpers.tool import *
from uuid import uuid1
import hashlib
from app.models.users import Users
auth = Blueprint('auth', __name__)


@auth.route('', methods=['POST'])
def login():
    data = {}
    telephone = request.values.get('telephone')
    password = request.values.get('password')
    if not telephone or not password:
        return jsonify(get_result("LACK_PARAMETER", data))
    user = Users.query.filter(Users.telephone == telephone).first()
    m2 = hashlib.md5(password)
    if user.password == m2.hexdigest():
        token = uuid1()
        data = {
            "id": user.id,
            "token": token,
            "telephone": telephone,
            "username": user.username
        }
        return jsonify(get_result("SUCCESS", data))
    else:
        return jsonify(get_result("WRONG_PASSWORD", data))

