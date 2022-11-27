import logging
from datetime import datetime
from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Date, Float, Boolean, DateTime, \
    UniqueConstraint, Index, Text
from sqlalchemy.orm import sessionmaker, mapper, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound, MultipleResultsFound
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
engine = create_engine('sqlite:///homework.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[hw_main]")


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, nullable=False)

    def __repr__(self):
        return F"The book {self.name}, in count: {self.count}, author_id: {self.author_id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)

    def __repr__(self):
        return f"The Author is {self.name}, id: {self.id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    surname = Column(String(20), nullable=False)
    phone = Column(String(10), nullable=False)
    email = Column(String(10), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"The student is {self.name}, id: {self.id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @classmethod
    def get_students_who_live_in_a_hostel(cls):
        try:
            student = session.query(Student).filter(Student.scholarship == True).all()
            return student
        except NoResultFound:
            logger.exception("NoResultFound for students who live in a hostel")
        except Exception as er:
            logger.exception(er)

    @classmethod
    def get_students_where_average_score_more(cls, score: float):
        try:
            student = session.query(Student).filter(Student.average_score > score).all()
            return student
        except NoResultFound:
            logger.exception("NoResultFound for students where average score >")
        except Exception as er:
            logger.exception(er)


class ReceiveBook(Base):
    __tablename__ = 'receiving_books'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    student_id = Column(Integer, nullable=False)
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    @hybrid_property
    def count_date_with_book(self):
        return self.date_of_return - self.date_of_return

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


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
        student_id=id_student,
        date_of_issue=date.date()
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
    return 'Книга спешно возвращена', 201


if __name__ == "__main__":
    app.run()
