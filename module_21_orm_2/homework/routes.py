import logging
from datetime import datetime
from models import Base, engine, session, Book, ReceiveBook, insert_data, Author
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("[routes]")


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    return 'Hello_world'


@app.route('/books', methods=['GET'])
def get_all_books():
    books = session.query(Book).all()
    book_list = []
    for book in books:
        book_list.append(book.to_json())
    return jsonify(book_list=book_list), 200


@app.route('/debtors', methods=['GET'])
def get_student_who_keep_book_more_14_days():
    receive_books = session.query(ReceiveBook).filter((ReceiveBook.date_of_return - ReceiveBook.date_of_issue) > 14)
    book_list = []
    for book in receive_books:
        book_list.append(book.to_json())
    return jsonify(students_id=book_list), 200


@app.route('/books', methods=['POST'])
def give_book_to_student():
    id_book = request.form.get('book_id', type=str)
    id_student = request.form.get('student_id', type=str)
    date = datetime.now()
    new_receiving_book = ReceiveBook(
        book_id=id_book,
        student_id=id_student
    )
    session.add(new_receiving_book)
    session.commit()
    return 'Книга успешно выдана', 201


@app.route('/books', methods=['PATCH'])
def return_book_to_the_library():
    id_book = request.form.get('book_id', type=str)
    id_student = request.form.get('student_id', type=str)
    return_date = datetime.now()
    from sqlalchemy import update
    try:
        query = update(ReceiveBook).where(ReceiveBook.book_id == id_book and ReceiveBook.student_id == id_student)\
            .values(date_of_return=return_date.date())
        session.execute(query)
    except NoResultFound:
        return 'student_id и book_id не найдено', 404
    return 'Книга успешно возвращена', 201


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    check_exist = session.query(Author).all()
    # insert_data()
    app.run(debug=True)
