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


class AddBookForm(FlaskForm):
    book_title = StringField(validators=[InputRequired()])
    author_name = StringField(validators=[InputRequired()])


def _get_html_table_for_books(books: list[dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows: str = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    # logger.debug(f'------>  {get_all_books()}')
    return render_template(
        'index.html',
        books=get_all_books(),
    )


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form():
    add_form = AddBookForm()
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
    return render_template('add_book.html')


@app.route('/books/<author_name>')
def get_book_by(author_name):
    logger.debug('[ENDPOINT IS][/books/<author_name>]')
    return render_template('show_books_by.html', books=get_book_by_author(author_name))


@app.route('/books/id/<id_book>')
def book_id(id_book):
    logger.debug(f'[ENDPOINT IS][/books/id/<id_book>] - book_id is - {id_book}')
    return render_template('show_books_by.html', books=get_book_by_id(id_book))


if __name__ == '__main__':
    init_db(DATA)
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
