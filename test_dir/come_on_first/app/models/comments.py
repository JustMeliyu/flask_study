# encoding:utf-8
from config import db
from datetime import datetime


class Comments(db.Model):
    """评论表"""
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    article = db.relationship('Articles', backref=db.backref('comments'))
    author = db.relationship('Users', backref=db.backref('comments'))
