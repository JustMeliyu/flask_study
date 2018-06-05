# encoding:utf-8

from flask import request, render_template, flash, redirect, url_for, Blueprint
from models import Users
from exts import db

register = Blueprint('register', __name__)


@register.route('/register/', methods=['GET', 'POST'])
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
            register_user = Users(telephone=telephone, username=username, password=password1)
            db.session.add(register_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
    return render_template('register.html')
