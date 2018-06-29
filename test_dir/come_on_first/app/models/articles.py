# encoding:utf-8
from config import db
from datetime import datetime


class Articles(db.Model):
    """文章表"""
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    author = db.relationship('Users', backref=db.backref('articles', lazy="dynamic"), lazy="select")

    def __repr__(self):
        # return "<article_id>: %r,%r,%r,%r" % (self.id, self.title, self.type, self.content)
        return "<article_id>: %r" % self.id

    def __init__(self, title, content, _type, author_id, create_time=None):
        self.title = title
        self.content = content
        self.type = _type
        self.create_time = create_time if create_time else datetime.now()
        self.author_id = author_id

    def get_articles(self, page_index, page_size, sort):
        pass

    @staticmethod
    def new(title, content, _type, author_id, create_time=None):
        article = Articles(title, content, _type, author_id, create_time)
        db.session.add(article)
        db.session.commit()
        return article

    def to_dict(self):
        dic = {}
        dic.update(self.__dict__)
        if "_sa_instance_state" in dic:
            del dic['_sa_instance_state']
        return dic
