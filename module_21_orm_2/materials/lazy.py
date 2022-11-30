from sqlalchemy import Column, Integer, ForeignKey, create_engine, Table
from sqlalchemy.orm import relationship, sessionmaker, backref, joinedload
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, primary_key=True)
    children = relationship("Child", lazy='select')  # lazy; select, joined, subquery, selectin, raise


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    parent = Parent()
    session.add(parent)
    child_one = Child(parent_id=1)
    child_two = Child(parent_id=1)
    session.add(child_one)
    session.add(child_two)
    session.commit()

    print('Запрос родителя')
    my_parent = session.query(Parent).first()

    print('Запрос детей')
    my_children = my_parent.children
    for c in my_children:
        print(c)

    print('custom lazy')
    q = session.query(Parent).options(joinedload(Parent.children)).all()

    print('end')
