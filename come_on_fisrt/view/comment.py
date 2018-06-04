# encoding:utf-8

from flask import session, request, url_for, redirect, Blueprint
from models import Articles, Users, Comments
from exts import db

comment = Blueprint('comment', __name__)


@comment.route('/comment/', methods=['POST'])
def publish_comment():
    print session.get('username')
    article_id = request.form.get('article_id')
    comment_content = request.form.get('comment')
    if session.get('username'):
        if comment_content:
            comment = Comments(content=comment_content)
            comment.article = Articles.query.filter(Articles.id == article_id).first()
            comment.author = Users.query.filter(Users.username == session.get('username')).first()
            db.session.add(comment)
            db.session.commit()
    return redirect(url_for('article.article_info', article_id=article_id))