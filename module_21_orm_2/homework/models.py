import logging
from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, Date, Float, Boolean, DateTime, \
    UniqueConstraint, Index, Text, ForeignKey
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


# class Book(Base):
#     __tablename__ = 'books'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20), nullable=False)
#     count = Column(Integer, default=1)
#     release_date = Column(Date, nullable=False)
#     author_id = Column(Integer, ForeignKey('authors.id'),  nullable=False)
#
#     receiving_book = relationship('ReceivingBook')
#
#     author = relationship("Author", backref=backref("books",
#                                                     cascade="all, "
#                                                             "delete-orphan",
#                                                     lazy="select"))
#
#     students = relationship('ReceivingBook', back_populates='book')
#
#     def __repr__(self):
#         return F"The book {self.name}, in count: {self.count}, author_id: {self.author_id}"
#
#     def to_json(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}
#
#
# class Author(Base):
#     __tablename__ = 'authors'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20), nullable=False)
#     surname = Column(String(20), nullable=False)
#     # books = relationship("Book")
#
#     def __repr__(self):
#         return f"The Author is {self.name}, id: {self.id}"
#
#     def to_json(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}
#
#
# class Student(Base):
#     __tablename__ = 'students'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20), nullable=False)
#     surname = Column(String(20), nullable=False)
#     phone = Column(String(10), nullable=False)
#     email = Column(String(10), nullable=False)
#     average_score = Column(Float, nullable=False)
#     scholarship = Column(Boolean, nullable=False)
#
#     def __repr__(self):
#         return f"The student is {self.name}, id: {self.id}"
#
#     def to_json(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}
#
#     @classmethod
#     def get_students_who_live_in_a_hostel(cls):
#         try:
#             student = session.query(Student).filter(Student.scholarship == True).all()
#             return student
#         except NoResultFound:
#             logger.exception("NoResultFound for students who live in a hostel")
#         except Exception as er:
#             logger.exception(er)
#
#     @classmethod
#     def get_students_where_average_score_more(cls, score: float):
#         try:
#             student = session.query(Student).filter(Student.average_score > score).all()
#             return student
#         except NoResultFound:
#             logger.exception("NoResultFound for students where average score >")
#         except Exception as er:
#             logger.exception(er)
#
#
# class ReceiveBook(Base):
#     __tablename__ = 'receiving_books'
#
#     id = Column(Integer, primary_key=True)
#     book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
#     student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
#     date_of_issue = Column(DateTime, nullable=False)
#     date_of_return = Column(DateTime, nullable=True)
#
#     @hybrid_property
#     def count_date_with_book(self):
#         return self.date_of_return - self.date_of_return
#
#     def to_json(self):
#         return {c.name: getattr(self, c.name) for c in self.__table__.columns}
#
#
# def insert_data():
#     authors = [Author(name="Александр", surname="Пушкин"),
#                Author(name="Лев", surname="Толстой"),
#                Author(name="Михаил", surname="Булгаков"),
#                ]
#     authors[0].books.extend([Book(name="Капитанская дочка",
#                                   count=5,
#                                   release_date=date(1836, 1, 1)),
#                              Book(name="Евгений Онегин",
#                                   count=3,
#                                   release_date=date(1838, 1, 1))
#                              ])
#     authors[1].books.extend([Book(name="Война и мир",
#                                   count=10,
#                                   release_date=date(1867, 1, 1)),
#                              Book(name="Анна Каренина",
#                                   count=7,
#                                   release_date=date(1877, 1, 1))
#                              ])
#     authors[2].books.extend([Book(name="Морфий",
#                                   count=5,
#                                   release_date=date(1926, 1, 1)),
#                              Book(name="Собачье сердце",
#                                   count=3,
#                                   release_date=date(1925, 1, 1))
#                              ])
#
#     students = [Student(name="Nik", surname="1", phone="2", email="3",
#                         average_score=4.5,
#                         scholarship=True),
#                 Student(name="Vlad", surname="1", phone="2", email="3",
#                         average_score=4,
#                         scholarship=True),
#                 ]
#     session.add_all(authors)
#     session.add_all(students)
#     session.commit()

# example:
#
# class Person(Model):
#     __tablename__ = 'persons'
#     id = Column(Integer, primary_key=True)
#     last_name = Column(Text, nullable=False)
#     groups = association_proxy('group_memberships', 'group')
#     # Other stuff
#
# class Group(Model):
#     __tablename__ = 'groups'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text, nullable=False)
#     members = association_proxy('group_memberships', 'person')
#     # Other stuff
#
# class GroupMembership(Model):
#     __tablename__ = 'group_memberships'
#     id = Column(Integer, primary_key=True)
#     person_id = Column(Integer, ForeignKey('persons.id'), nullable=False)
#     group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
#     person = relationship('Person', uselist=False, backref=backref('group_memberships', cascade='all, delete-orphan'))
#     group = relationship('Group', uselist=False, backref=backref('group_memberships', cascade='all, delete-orphan'))
#     # Other stuff


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(100), nullable=False)

    def __repr__(self):
        return f"The Author is {self.name}, id: {self.id}"

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
        print(a_query)

    # task 2.2
    input_student_id = 1
