import logging
from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Date, Float, Boolean, DateTime, \
    UniqueConstraint, Index, Text, ForeignKey, func
from sqlalchemy.orm import sessionmaker, mapper, declarative_base, relationship, backref, joinedload
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from datetime import date, datetime
from pprint import pprint

engine = create_engine('sqlite:///homework.db', echo=False, connect_args={"check_same_thread": False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[models]")


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), nullable=False)

    def __repr__(self):
        return f"The Author is {self.name},surname is {self.surname}, id: {self.id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)  # foreing_key для ссылки на таблицу авторов

    author = relationship("Author", backref=backref("books",
                                                    cascade="all, "
                                                            "delete-orphan",
                                                    lazy="select"))  # определили связь через обратную ссылку backref,
    # backref передали параметры cascade, lazy. all, dalete-orphan - смотрим на все каскадные поведения,
    # lazy=select - подгружаем авторов по запросу

    # students = relationship('ReceivingBook', back_populates='book')

    students = association_proxy('ReceivingBook', 'person')

    def __repr__(self):
        return F"The book {self.name}, in count: {self.count}, author_id: {self.author_id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), nullable=False)
    phone = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)

    # books = relationship('ReceivingBook', back_populates='student')  # связь student с receiving_book через поле books

    books = association_proxy('ReceivingBook', 'book')

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


class ReceivingBook(Base):
    __tablename__ = 'receiving_books'

    book_id = Column(Integer, ForeignKey('books.id'),
                     primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'),
                        primary_key=True)

    date_of_issue = Column(DateTime, default=datetime.now)
    date_of_finish = Column(DateTime, nullable=True)

    # связь many to many в декларативном стиле
    # student = relationship("Student", back_populates="books")  # двунаправленная связь со студентами
    # book = relationship("Book", back_populates="students")  # двунаправленная связь с книгами

    student = relationship('Student', backref=backref('receiving_books', cascade='all, delete-orphan'))
    book = relationship('Book', backref=backref('receiving_books', cascade='all, delete-orphan'))

    def __repr__(self):
        return f'book_id-[{self.book_id}], student_id-[{self.student_id}], date_of_issue-[{self.date_of_issue}], ' \
               f'date_of_finish-[{self.date_of_finish}]'

    @hybrid_property
    def count_date_with_book(self):
        return self.date_of_return - self.date_of_return

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def insert_data():
    authors = [Author(name="Александр", surname="Пушкин"),
               Author(name="Лев", surname="Толстой"),
               Author(name="Михаил", surname="Булгаков"),
               ]
    authors[0].books.extend([Book(name="Капитанская дочка",
                                  count=5,
                                  release_date=date(1836, 1, 1)),
                             Book(name="Евгений Онегин",
                                  count=3,
                                  release_date=date(1838, 1, 1))
                             ])
    authors[1].books.extend([Book(name="Война и мир",
                                  count=10,
                                  release_date=date(1867, 1, 1)),
                             Book(name="Анна Каренина",
                                  count=7,
                                  release_date=date(1877, 1, 1))
                             ])
    authors[2].books.extend([Book(name="Морфий",
                                  count=5,
                                  release_date=date(1926, 1, 1)),
                             Book(name="Собачье сердце",
                                  count=3,
                                  release_date=date(1925, 1, 1))
                             ])

    students = [Student(name="Nik", surname="1", phone="2", email="3",
                        average_score=4.5,
                        scholarship=True),
                Student(name="Vlad", surname="1", phone="2", email="3",
                        average_score=4,
                        scholarship=True),
                ]
    session.add_all(authors)
    session.add_all(students)
    session.commit()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    check_exist = session.query(Author).all()
    if not check_exist:
        insert_data()

    # task 2.1
    input_author_id = 1
    author_query = session.query(Author).filter(Author.id != 1).all()
    # pprint(author_query)
    for a_query in author_query:
        # print(a_query)
        ...

    # task 2.2
    input_student_id = 3
    get_book_id = session.query(ReceivingBook).filter(ReceivingBook.student_id == input_student_id).all()
    book_id_from_receive = 0
    for g_query in get_book_id:
        book_id_from_receive = g_query.book_id
    a = """
    SELECT authors.name as author_name
    FROM authors
    JOIN books
    ON authors.id = books.author_id
    WHERE books.id != (
    SELECT book_id
    FROM receiving_books
    WHERE student_id = 3)
    """
    # res = session.query(Author.id).join(Book).filter(Book.id == book_id_from_receive).one_or_none()
    # print(res[0])
    all_book_without_author = session.query(Author).filter(Author.id != (session.query(Author.id).join(Book).filter(Book.id == book_id_from_receive).one_or_none())[0]).all()
    for one_author in all_book_without_author:
        print(one_author)

    # task 2.3
    date_mounth = 12
    all_book_uniq_id_from_receive_table = """
    SELECT count(*)
    FROM
    (SELECT book_id
    FROM receiving_books
    where date_of_issue > 12
    GROUP by book_id)
    """
    all_book_from_book_table = """
    SELECT count(*)
    FROM books
    """
    books_where_date = session.query(ReceivingBook).filter(ReceivingBook.date_of_issue > date_mounth).\
        group_by(ReceivingBook.book_id).all()
    print(books_where_date)
    print(len(books_where_date))
    all_books = session.query(Book).all()
    print(len(all_books))
    avg_books = len(all_books) / len(books_where_date)
    print(avg_books)

    # task 2.4
    sql_req = """
    SELECT *
    FROM receiving_books
    WHERE receiving_books.student_id = 
    (SELECT students.id
    FROM students
    WHERE students.average_score > 4)
    """

