import logging
import csv
from datetime import datetime, date
from sqlalchemy import func
from models import Base, engine, session, Book, ReceivingBook, insert_data, Author, Student
from sqlalchemy.exc import NoResultFound, MultipleResultsFound, InvalidRequestError
from flask import Flask, jsonify, abort, request, flash


UPLOAD_FOLDER = '/files'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'csv'}
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
def all_book_in_month():
    """Получите среднее количество книг, которые студенты брали в этом месяце"""
    current_month = f'{date.today():%m%Y}'
    route_logger.debug(current_month)
    books_in_month = session.query(ReceivingBook, func.avg(ReceivingBook.book_id)) \
        .filter(func.strftime(ReceivingBook.date_of_issue, '%m%Y') == current_month).group_by(ReceivingBook.student_id).all()
    route_logger.debug(books_in_month)
    return jsonify(data=[i for i in books_in_month]), 200


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
def top_10_students_year():
    """Получите ТОП-10 самых читающих студентов в этом году"""
    current_year = f'{date.today():%Y}'
    top_10_students = session.query(func.count(ReceivingBook.date_of_issue), Student.name, Student.surname).join(
        Student) \
        .filter(func.strftime(ReceivingBook.date_of_issue, '%Y') == current_year).group_by(ReceivingBook.student_id) \
        .order_by(func.count(ReceivingBook.date_of_issue).desc()).limit(10)

    route_logger.debug(top_10_students)
    return jsonify(data=[i for i in top_10_students]), 200


@app.route('/students/insert_csv', methods=['POST'])
def import_csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            route_logger.debug('NO FILE')
        # file_form = request.files['students.csv']
    csv_file = 'file_form'
    for req_file in request.files:
        route_logger.debug(req_file)
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['name'], row['surname'], row['phone'], row['email'], row['average_score'], row['scolarship'])
    return {'key': 'value'}


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    check_exist = session.query(Author).all()
    if not check_exist:
        insert_data()
    app.run(debug=True)
