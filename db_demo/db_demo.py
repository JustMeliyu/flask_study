# encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)
print app.config['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)
# create table users(
#     id int primary key autoincrement,
#     username varchar(100) not null
# )
# create table article(
#     id int primary key  autoincrement,
#     title varchar(100) not null,
#     content text not null
#     author_id int,
#     foreign key 'author_id' references 'users.id'
# )


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)


class Articles(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    author = db.relationship('Users', backref=db.backref('articles'))


# class Persions(db.Model):
#     __tablename__ = 'persions'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     lastname = db.Column(db.String(100), nullable=False)
#     firstname = db.Column(db.String(100), nullable=False)


db.create_all()


# @app.route('/')
# def index():
#     # 增加
#     # article1 = Article(title='aaa', content='bbb')
#     # db.session.add(article1)
#     # # 事物
#     # db.session.commit()
#
#     # 查
#     # select * from article where title='aaa'
#     # article1 = Article.query.filter(Article.title == 'ccc').first()
#     # print article1.title
#     # print article1.content
#
#     # 改
#     # article1.title = 'ccc'
#     # article1.content = 'ddd'
#     # db.session.commit()
#
#     # 删
#     # db.session.delete(article1)
#     # db.session.commit()
#     return 'index'

@app.route('/')
def index():
    # user1 = Users(username='ly')
    # db.session.add(user1)
    # db.session.commit()

    # article1 = Articles(title='aaa', content='bbb')
    # article1.author = Users.query.filter(Users.id == 1).first()
    # article2 = Articles(title='ccc', content='ddd')
    # article2.author = Users.query.filter(Users.id == 1).first()
    # article3 = Articles(title='eee', content='fff')
    # article3.author = Users.query.filter(Users.username == 'ly').first()
    # db.session.add(article3)
    # # db.session.add(article2)
    # db.session.commit()
    # article4 = Articles.query.filter(Articles.id == 1).first()
    # print article4.author.username
    #
    # user1 = Users.query.filter(Users.username == 'ly').first()
    # result = user1.articles
    # for r in result:
    #     print '-'*10
    #     print r.title, r.content
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
