# encoding:utf-8

from flask import render_template, Blueprint

not_found = Blueprint('not_found_404', __name__)


@not_found.route('')
def not_found_404():
    return render_template('404.html')
