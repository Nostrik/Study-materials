import logging
from datetime import datetime

from sqlalchemy import func

from models import Base, engine, session, Book, ReceivingBook, insert_data, Author, Student
from sqlalchemy.exc import NoResultFound, MultipleResultsFound, InvalidRequestError
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
route_logger = logging.getLogger("[routes]")


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/')
def hello_world():
    return 'Hello_world'


@app.route('/books', methods=['GET'])
def get_all_books():
    books = session.query(Book).all()
    route_logger.debug(books)
    book_list = []
    for book in books:
        book_list.append(book.to_json())
    return jsonify(book_list=book_list), 200


@app.route('/debtors', methods=['GET'])
def get_student_who_keep_book_more_14_days():
    receive_books = session.query(ReceivingBook).filter((ReceivingBook.date_of_return - ReceivingBook.date_of_issue)
                                                        > 14)
    book_list = []
    for book in receive_books:
        book_list.append(book.to_json())
    return jsonify(students_id=book_list), 200


@app.route('/books', methods=['POST'])
def give_book_to_student():
    id_book = request.form.get('book_id', type=str)
    id_student = request.form.get('student_id', type=str)
    new_receiving_book = ReceivingBook(
        book_id=id_book,
        student_id=id_student
    )
    route_logger.debug(new_receiving_book)
    session.add(new_receiving_book)
    session.commit()
    return 'Книга успешно выдана', 201


@app.route('/books', methods=['PATCH'])
def return_book_to_the_library():
    id_book = request.form.get('book_id')
    id_student = request.form.get('student_id', type=str)
    return_date = datetime.now()
    route_logger.debug(return_date)
    from sqlalchemy import update
    try:
        query = update(ReceivingBook).where(ReceivingBook.book_id == id_book)\
            .values(date_of_finish=return_date)
        # query2 = ReceivingBook.update().values(date_of_finish=return_date).where(ReceivingBook.book_id == id_book)
        session.execute(query)
    except NoResultFound:
        return 'student_id и book_id не найдено', 404
    return 'Книга успешно возвращена', 201


@app.route('/books/<int:author_id>/count_by_author', methods=['GET'])
def get_books_by_author(author_id: int):
    """Получите количество оставшихся в библиотеке книг по автору"""
    # author_id = request.args.get('author_id')
    route_logger.debug(author_id)
    quantity_books_by_author = session.query(func.sum(Book.count)).filter(Book.author_id != author_id).scalar()
    return jsonify(books_count=quantity_books_by_author), 200


@app.route('/books/<int:student_id>/no_read', methods=['GET'])
def not_read_books(student_id: int):
    """Получите список книг, которые студент не читал, при этом другие книги этого автора студент уже брал"""
    route_logger.debug(student_id)
    read_books = session.query(Book.id, Book.author_id).join(ReceivingBook) \
        .filter(ReceivingBook.student_id == student_id).all()
    authors_list = [i[1] for i in read_books]
    books_list = [i[0] for i in read_books]

    route_logger.debug(authors_list)
    route_logger.debug(books_list)

    not_read_books = session.query(Book) \
        .filter(Book.author_id.in_(authors_list)) \
        .filter(Book.id.not_in(books_list)).all()
    res = [i.to_json() for i in not_read_books]
    route_logger.debug(res)
    return jsonify(books_list=res), 200


@app.route('/books/avg', methods=['GET'])
def func_name2():
    """Получите среднее количество книг, которые студенты брали в этом месяце"""
    ...


@app.route('/books/popular', methods=['GET'])
def popular_book():
    """Получите самую популярную книгу среди студентов, у которых средний балл больше 4.0"""
    most_popular_book = session.query(Book.name, Author.name, Author.surname,
                                      func.count(ReceivingBook.date_of_issue)).join(Author) \
        .join(ReceivingBook).join(Student).filter(Student.average_score > 4.0) \
        .order_by(ReceivingBook.date_of_issue.desc()).limit(1).one_or_none()
    route_logger.debug(most_popular_book)
    return jsonify(books_list=[i for i in most_popular_book]), 200


@app.route('/books/top', methods=['GET'])
def func_name4():
    """Получите ТОП-10 самых читающих студентов в этом году"""
    top_10_students = session.query(ReceivingBook.date_of_issue, Student.name, Student.surname).join(Student) \
        .filter()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    check_exist = session.query(Author).all()
    if not check_exist:
        insert_data()
    app.run(debug=True)
