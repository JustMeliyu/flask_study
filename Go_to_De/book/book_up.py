# encoding:utf-8

from flask import Blueprint, url_for, render_template, request, flash, redirect

book_up = Blueprint(
    'book',
    __name__,
    template_folder='../templates',
)
books = ['The Name of the Rose', 'The Historian', 'Rebecca']


@book_up.route('/', method=['GET'])
def index():
    return 'book'


@book_up.route('/book', method=['GET', 'POST'])
def handle_book():
    _form = request.form()

    if request.method == 'POST':
        title = _form["title"]
        books.append(title)
        flash('add book successfully')
        return redirect(url_for('book.handle_book'))

    return render_template(
        'book.html',
        books=books
    )
