from flask import Flask, render_template
from flask import request
from models import init_db, get_all_books, DATA, add_new_book, get_book_by_author, get_book_by_id
import logging
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

app: Flask = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[from routes]')


class BookForm(FlaskForm):
    book_title = StringField(validators=[InputRequired()])
    author_name = StringField(validators=[InputRequired()])


class SearchAuthorForm(FlaskForm):
    author_name = StringField(validators=[InputRequired()])


class SearchIdForm(FlaskForm):
    book_id = StringField(validators=[InputRequired()])


@app.route('/books')
def all_books() -> str:
    return render_template(
        'index.html',
        books=get_all_books(),
    )


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form():
    add_form = BookForm()
    if request.method == 'POST':
        if add_form.validate_on_submit():
            # title = request.form.get('book_title')
            # author = request.form.get('author_name')
            # title = request.form['book_title']
            # author = request.form['author_name']
            title, author = add_form.book_title.data, add_form.author_name.data
            logger.debug(f'title is - {title}')
            logger.debug(f'author is - {author}')
            add_new_book(title, author)
            return f'Book added successful'
        return f"Invalid input, {add_form.errors}", 400
    return render_template('add_book.html', form=add_form)


@app.route('/books/author', methods=['GET', 'POST'])
def get_book_by():
    form = SearchAuthorForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            author_name = form.author_name.data
            logger.debug(f'f[POST][/books/<author_name>] - author_name is - {author_name}')
            books = get_book_by_author(author_name)
            return render_template('show_books_by.html', books=books, form=form)
        return f"Invalid input, {form.errors}", 400
    logger.debug('[GET][/books/<author_name>]')
    return render_template('show_books_by.html', form=form)


@app.route('/books/id', methods=['GET', 'POST'])
def book_id():
    form = SearchIdForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            book = form.book_id.data
            logger.debug(f'[ENDPOINT IS][/books/id/<id_book>] - book_id is - {book}')
            books = get_book_by_id(book)
            return render_template('show_book_by_id.html', books=books, form=form)
        return f"Invalid input, {form.errors}", 400
    return render_template('show_book_by_id.html', form=form)


if __name__ == '__main__':
    init_db(DATA)
    app.config["SECRET_KEY"] = '123654789aaa'
    # app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
