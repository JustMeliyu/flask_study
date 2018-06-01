# encoding: utf-8

from exts import db


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    tag = db.Column(db.String(100), nullable=False)
    # tags = db.relationship('Tag', secondary='article_tag', backref=db.backref('articles'))
