# encoding:utf-8

from flask import session, request, url_for, redirect, Blueprint, flash
from app.models.articles import Articles
from app.models.users import Users
from app.models.comments import Comments
from config import db

comment = Blueprint('comment', __name__)


@comment.route('/comment/', methods=['POST'])
def publish_comment():
    article_id = request.form.get('article_id')
    comment_content = request.form.get('comment').strip()
    if session.get('username'):
        if comment_content:
            comment = Comments(content=comment_content)
            comment.article = Articles.query.filter(Articles.id == article_id).first()
            comment.author = Users.query.filter(Users.username == session.get('username')).first()
            db.session.add(comment)
            db.session.commit()
        else:
            flash(u'评论不能为空', 'error')
        return redirect(url_for('article.article_info', article_id=article_id))
    return redirect(url_for('auth.login'))

