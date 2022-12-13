import logging
from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Date, Float, Boolean, DateTime, \
    UniqueConstraint, Index, Text, ForeignKey, func
from sqlalchemy.orm import sessionmaker, mapper, declarative_base, relationship, backref, joinedload
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from datetime import date, datetime, timedelta
from pprint import pprint

engine = create_engine('sqlite:///homework.db', echo=False, connect_args={"check_same_thread": False})
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
logging.basicConfig(level=logging.DEBUG)
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

    @hybrid_method
    def is_debtors(self, compare_date):
        return self.date_of_issue < compare_date

    @hybrid_method
    def is_month(self, current_month: str):
        return current_month < self.date_of_issue

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
    sql_2_1 = """
    SELECT sum(books.count)
    FROM books
    WHERE books.author_id = 1
    """
    input_author_id = 1
    quantity_books_by_author = session.query(func.sum(Book.count)).filter(Book.author_id != 1).scalar()
    # print('quantity_books_by_author')
    # print(quantity_books_by_author)
    print('=' * 100)

    # task 2.2
    input_student_id = 3
    print('task 2.2')
    read_books = session.query(Book.id, Book.author_id).join(ReceivingBook)\
        .filter(ReceivingBook.student_id == input_student_id).all()
    authors_list = [i[1] for i in read_books]
    books_list = [i[0] for i in read_books]

    not_read_books = session.query(Book) \
        .filter(Book.author_id.in_(authors_list)) \
        .filter(Book.id.not_in(books_list)).all()
    res = [i for i in not_read_books]
    print(res)
    print('=' * 100)

    # task 2.3
    print('task 2.3')
    all_book_uniq_id_from_receive_table = """
    SELECT student_id, AVG(book_id) as Average_books
        FROM receiving_books
    WHERE strftime('%m%Y', date_of_issue) = strftime('%m%Y', date('now')) 
    GROUP BY student_id;
    """
    current_month = datetime.now()
    current_month_1 = current_month.month + 1
    sql_2_3 = session.query(ReceivingBook, func.avg(ReceivingBook.book_id))\
        .filter(ReceivingBook.date_of_issue).group_by(ReceivingBook.student_id).all()
    print(sql_2_3)
    print('=' * 100)

    # task 2.4
    sql_req = """
    SELECT COUNT(r.date_of_issue) as RAZ, a.name, a.surname, b.name 
        FROM books b INNER JOIN authors a
        ON b.author_id = a.id
            INNER JOIN receiving_books r
            ON r.book_id=b.id
                INNER JOIN students s
                ON s.id = r.student_id
    WHERE s.average_score>4.0
    GROUP BY b.id
    ORDER BY RAZ DESC
    LIMIT 1;
    """
    print('task 2.4')
    most_popular_book = session.query(Book.name, Author.name, Author.surname, func.count(ReceivingBook.date_of_issue)).join(Author)\
        .join(ReceivingBook).join(Student).filter(Student.average_score > 4.0)\
        .order_by(ReceivingBook.date_of_issue.desc()).limit(1)
    print('=' * 100)
    print(most_popular_book)

    # task 2.5
    sql_req2 = """
    SELECT COUNT(r.date_of_issue) as RAZ, s.name, s.surname
    FROM receiving_books r
        INNER JOIN students s
        ON s.id = r.student_id
    WHERE strftime('%Y', date_of_issue) = strftime('%Y', date('now')) 
    GROUP BY r.student_id
    ORDER BY RAZ DESC
    LIMIT 10;
    """
    print('=' * 100)
    top_10_students = session.query(func.count(ReceivingBook.date_of_issue), Student.name, Student.surname).join(Student)\
        .filter(ReceivingBook.date_of_issue == 12).group_by(ReceivingBook.student_id)\
        .order_by(func.count(ReceivingBook.date_of_issue).desc()).limit(10)
    print(top_10_students)

