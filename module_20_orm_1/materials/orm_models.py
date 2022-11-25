if __name__ == "__main__":
    from sqlalchemy import Table, create_engine, MetaData, Column, Integer, String, UniqueConstraint, Index
    from sqlalchemy.orm import sessionmaker, mapper, declarative_base
    from sqlalchemy.exc import NoResultFound, MultipleResultsFound

    engine = create_engine("sqlite:///python.db")
    Session = sessionmaker(bind=engine)
    session = Session()

#  declarative style
    Base = declarative_base(bind=engine)

    class User(Base):
        __tablename__ = 'user'
        # __table_args__ = {'schema': 'some_schema'}
        __table_args__ = (Index('email_index', 'email'))
        __maper_args__ = ''

        id = Column('id', Integer, primary_key=True)
        name = Column('name', String(16), nullable=False)
        email = Column('email', String(16))
        login = Column('login', String(16), nullable=False)

        def __repr__(self):
            return f"{self.name}, {self.email}, {self.login}"

        @classmethod
        def get_all_users(cls):
            return session.query(User).all()

        @classmethod
        def get_user_by_email(cls, email: str):
            try:
                user = session.query(User).filter(User.email == email).one()
                return user
            except NoResultFound:
                print(f'User with {email} does not exists')
            except MultipleResultsFound:
                print(f'Uniq index error')

    Base.metadata.create_all()

#  classic style
    # metadata = MetaData(bind=engine)
    #
    # users = Table('users', metadata,
    #               Column('id', Integer, primary_key=True),
    #               Column('name', String(16), nullable=False),
    #               Column('email', String(16)),
    #               Column('login', String(16), nullable=False)
    #               )
    #
    #
    # class User:
    #     def __init__(self, name, email, login):
    #         self.name = name
    #         self.email = email
    #         self.login = login
    #
    #     def __repr__(self):
    #         return f"{self.name}, {self.email}, {self.login}"
    #
    #
    # mapper(User, users)
    # metadata.create_all()

