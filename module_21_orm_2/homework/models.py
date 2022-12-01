import logging
from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Date, Float, Boolean, DateTime, \
    UniqueConstraint, Index, Text, ForeignKey
from sqlalchemy.orm import sessionmaker, mapper, declarative_base, relationship, backref
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from datetime import date

engine = create_engine('sqlite:///homework.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[models]")


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'),  nullable=False)

    author = relationship("Author", backref=backref(
        "books", cascade="all, delete-orphan", lazy="select"
    ))
    students = relationship('RecievingBook', back_populates='book')

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

    books = relationship('ReceivingBook', back_populates='student')

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
    date_of_return = Column(DateTime, nullable=True)

    student = relationship("Student", back_populates="books")
    book = relationship("Book", back_populates="students")

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
