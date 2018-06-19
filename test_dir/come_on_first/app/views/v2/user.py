# encoding:utf-8
from flask import session, render_template, redirect, url_for, Blueprint

user = Blueprint('user', __name__)


@user.route('<username>')
def user_info(username):
    if session.get('username') == username:
        return render_template('user.html')
    else:
        return redirect(url_for('auth.login'))
