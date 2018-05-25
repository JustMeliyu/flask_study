from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)


# class Users(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(100), nullable=False)
#
#
# class Articles(db.Model):
#     __tablename__ = 'articles'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     content = db.Column(db.String(100), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    tags = db.relationship('Tag', secondary='article_tag', backref=db.backref('articles'))


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


article_tag = db.Table(
    'article_tag',
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
)


db.create_all()


@app.route('/')
def hello_world():
    # article1 = Article(title='aaa')
    # article2 = Article(title='bbb')
    # tag1 = Tag(name='ccc')
    # tag2 = Tag(name='ddd')
    #
    # article1.tags.append(tag1)
    # article1.tags.append(tag2)
    #
    # article2.tags.append(tag1)
    # article2.tags.append(tag2)
    #
    # db.session.add(article1)
    # db.session.add(article2)
    # db.session.add(tag1)
    # db.session.add(tag2)
    #
    # db.session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
