# encoding:utf-8

from flask import session, request, redirect, render_template, url_for, Blueprint, flash
from app.models.articles import Articles
from app.models.users import Users
from config import db

publish = Blueprint('publish', __name__)


@publish.route('', methods=['GET', 'POST'])
def publish_article():
    if session.get('username'):
        if request.method == 'GET':
            return render_template('publish.html')
        else:
            article_type = request.values.get('article_type')
            title = request.form.get('title').strip()
            content = request.form.get('content').strip()
            if title and content:
                article = Articles(type=article_type, title=title, content=content)
                author = Users.query.filter(Users.username == session['username']).first()
                article.author = author
                db.session.add(article)
                db.session.commit()
                return redirect(url_for('article.article_info', article_id=article.id))
            else:
                flash(u'标题或内容不能为空', 'error')
                return render_template('publish.html')
    else:
        return redirect(url_for('auth.login'))
