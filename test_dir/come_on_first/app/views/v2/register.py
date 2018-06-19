# encoding:utf-8

from flask import request, render_template, flash, redirect, url_for, Blueprint
from app.models.users import Users
from config import db
import hashlib

register = Blueprint('register', __name__)


@register.route('', methods=['GET', 'POST'])
def register_auth():
    if request.method == 'POST':
        telephone = request.form.get('telephone').strip()
        username = request.form.get('username').strip()
        password1 = request.form.get('password1').strip()
        password2 = request.form.get('password2').strip()
        register_user = Users.query.filter(Users.telephone == telephone).first()
        # 如果手机号以填写，则弹出提示
        if not telephone:
            flash(u'手机号不能为空', 'error')
        elif not username:
            flash(u'用户名不能为空', 'error')
        elif not password1 or not password2:
            flash(u'密码不能为空', 'error')
        elif register_user:
            flash(u'该手机号以注册，请重新输入', 'error')
        elif password1 != password2:
            flash(u'两次输入的密码不一致，请重新输入', 'error')
        else:
            m2 = hashlib.md5(password1)
            register_user = Users(telephone=telephone, username=username, password=m2.hexdigest())
            db.session.add(register_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('register.html')
