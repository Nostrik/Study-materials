from sqlalchemy import Column, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///one_to_many.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Parent(Base):
    __tablename__ = 'parent'

    id = Column(Integer, primary_key=True)
    children = relationship("Child", back_populates="parent")
    # двунаправленная связь
    # children = relationship("Child", back_populates="parent")
    # альтернативный вариант
    # children = relationship("Child", back_ref="parent")

    # many to one
    # child_id = Column(Integer, ForeignKey('child.id'))
    # child = relationship("Child")


class Child(Base):
    __tablename__ = 'child'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parent = relationship("parent", back_populates="children")


# связываем родительскую таблицу в класичесском стиле представления
# mapper(PArent, properties={
#     'children': relationship(Child)
# })

if __name__ == '__main__':

    Base.metadata.create_all(engine)
    parent = Parent()
    session.add(parent)
    session.commit()
    child_one = Child(parent_id=1)
    child_two = Child(parent_id=1)
    session.add(child_one)
    session.add(child_two)
    session.commit()

    my_children = session.query(Child).filter(Child.parent_id==1).all()
    my_parent = session.query(Parent).first()

    print('ok')
