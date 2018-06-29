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
    article = db.relationship('Articles', backref=db.backref('comments', lazy="dynamic"))
    author = db.relationship('Users', backref=db.backref('comments', lazy="dynamic"))

    def __init__(self, content, article_id, user_id, create_time=None):
        self.content = content
        self.article_id = article_id
        self.user_id = user_id
        self.create_time = create_time if create_time else datetime.now()

    @staticmethod
    def new(content, article_id, user_id, create_time=None):
        comment = Comments(content, article_id, user_id, create_time)
        db.session.add(comment)
        db.session.commit()
        return comment

    def to_dict(self):
        dic = {}
        dic.update(self.__dict__)
        if "_sa_instance_state" in dic:
            del dic['_sa_instance_state']
        return dic
