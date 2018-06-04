# encoding:utf-8

from flask import request, render_template, flash, redirect, url_for, Blueprint
from models import Users
from exts import db
# from . import db

register = Blueprint('register', __name__)


@register.route('/register/', methods=['GET', 'POST'])
def register_auth():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        register_user = Users.query.filter(Users.telephone == telephone).first()
        # 如果手机号以填写，则弹出提示
        if register_user:
            flash('该手机号以注册，请重新输入；', 'error')
            return render_template('register.html')
        else:
            # 两次输入的密码需保持一致
            if password1 != password2:
                flash('两次输入的密码不一致，请重新输入；', 'error')
                return render_template('register.html')
            elif password1 == '':
                flash('密码不能为空；', 'error')
                return render_template('register.html')
            else:
                register_user = Users(telephone=telephone, username=username, password=password1)
                db.session.add(register_user)
                db.session.commit()
                return redirect(url_for('auth.login'))
