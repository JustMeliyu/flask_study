# encoding:utf-8

from flask import Blueprint, render_template, url_for, redirect
from app.models.comments import Comments
from app.models.articles import Articles
from app.helpers.tool import class_to_dict

article = Blueprint('article', __name__,)


@article.route('<article_id>', methods=['GET', 'POST'])
def article_info(article_id):
    all_comments = []
    current_article = Articles.query.filter(Articles.id == article_id).first()
    if current_article:
        # 显示文章
        current_article.create_time = current_article.create_time.strftime('%Y-%m-%d %H:%M:%S')
        article_info = class_to_dict(current_article)
        article_info['author'] = current_article.author.username
        # 显示评论
        comments = Comments.query.filter(Comments.article_id == article_id).all()
        for c in comments:
            author = c.author.username
            c = class_to_dict(c)
            c['author'] = author
            all_comments.append(c)
        return render_template('article.html', article=article_info, comments=all_comments)
    else:
        return redirect(url_for('not_found.not_found_404'))


@article.route('/article/')
def all_articles():
    all_articles = []
    # 显示所有文章
    articles = Articles.query.all()
    for article in articles:
        author = article.author.username
        article = class_to_dict(article)
        article['author'] = author
        article['content'] = article['content'][0:40] + '......'
        all_articles.append(article)
    return render_template('all_article.html', articles=all_articles)
