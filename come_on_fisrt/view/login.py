# encoding:utf-8

from flask import Blueprint, redirect, request,render_template, flash, session, url_for
from models import Users
from datetime import timedelta
from config import app
from services.public import class_to_dict
from uuid import uuid1
from helpers.tools import *
auth = Blueprint('auth', __name__)

#
# @auth.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return render_template('login.html')
#     else:
#         re = class_to_dict(request)
#         # for k, v in re.get('environ').items():
#         #     print "%s ：%s" % (k, v)
#         # print request.get_json(force=False, silent=True)
#         telephone = request.form.get('telephone')
#         password = request.form.get('password')
#         remember_me = request.form.get('remember_me')
#         if remember_me:
#             session.permanent = True
#             app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
#         # 判断用户名是否存在
#         if password == '' or telephone == '':
#             flash(u'用户名或密码不能为空', 'error')
#             return render_template('login.html')
#         else:
#             current_user = Users.query.filter(Users.telephone == telephone).first()
#         if not current_user:
#             flash(u'该用户不存在，请重新输入', 'error')
#             return render_template('login.html')
#         else:
#             # 判断密码是否正确
#             if current_user.password != password:
#                 flash(u'密码错误，请重新输入', 'error')
#                 return render_template('login.html')
#             else:
#                 session['telephone'] = current_user.telephone
#                 session['username'] = current_user.username
#                 return redirect(url_for('index.index_page'))


# @auth.route('/logout/')
# def logout():
#     session.clear()
#     return redirect(url_for('index.index_page'))

@auth.route('/login/', methods=['POST'])
def login():
    data = {}
    telephone = request.values.get('telephone')
    password = request.values.get('password')
    # if telephone == "" or password == "" or telephone is None or password is None:
    if not telephone or not password:
        return jsonify(get_result("LACK_PARAMETER", data))
    user = Users.query.filter(Users.telephone == telephone).first()
    if user.password == password:
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


