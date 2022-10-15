from flask import Flask, render_template
from flask import request
from models import init_db, get_all_books, DATA, add_new_book
import logging
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

app: Flask = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AddBookForm(FlaskForm):
    book_title = StringField(validators=[InputRequired])
    book_author = StringField(validators=[InputRequired])


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
    return render_template(
        'index.html',
        books=get_all_books(),
    )


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form():
    add_form = AddBookForm()
    if request.method == 'POST':
        # title = request.form.get('book_title')
        # author = request.form.get('author_name')
        # title = request.form['book_title']
        # author = request.form['author_name']
        title, author = add_form.book_title, add_form.book_author
        add_new_book(title, author)
        logger.debug(f'title is - {title}')
        logger.debug(f'author is - {author}')
        return f'Book added successful'
    return render_template('add_book.html')
    # return f"Invalid input, {add_form.errors}", 400
    # return render_template('add_book.html')


if __name__ == '__main__':
    init_db(DATA)
    app.run(debug=True)
