from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
from datetime import datetime
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# class Registration(db.Model):
#     __tablename__ = "registrantion"
#     article_id = db.Column(db.Integer, db.ForeignKey('article.id'), primary_key=True)
#     tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)
#     create_at = db.Column(db.DateTime, default=datetime.utcnow)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    tags = db.relationship("article_tag",
                           backref=db.backref('articles', lazy="joined"), lazy="dynamic")

    def __repr__(self):
        return '<class: %r>' % self.title


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    articles = db.relationship("article_tag",
                               backref=db.backref('tags', lazy="joined"), lazy="dynamic")

    def __repr__(self):
        return '<class: %r>' % self.name


article_tag = db.Table(
    'article_tag',
    db.Column("article_id", db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column("tag_id", db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


db.create_all()
art = Article.query.filter_by(id=1).first()
print("=======")
print art
print art.tags
# print art.tags.all()
tag = Tag.query.filter_by(id=1).first()
# print tag.articles.all()
# r = Registration()


@app.route('/')
def hello_world():

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
