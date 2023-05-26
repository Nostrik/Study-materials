from sqlalchemy import Column, Integer, ForeignKey, create_engine, Table
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

intergration_table = Table('integrations', Base.metadata,
                           Column('parent_id', ForeignKey('parent_id'), primary_key=True),
                           Column('child_id', ForeignKey('child_id'), primary_key=True)
                           )


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    # children = relationship("Child", secondary=integration_table)

    # двунаправленная связь
    children = relationship("Child", secondary=intergration_table, back_populates="parents")

    # определение с помощью back_ref
    # children = relationship("Child", secondary=intergration_table, backref="parents")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)

    # двунаправленная связь
    parents = relationship(
        "Parent",
        secondary=intergration_table,
        back_populates="Children"
    )


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

    father = Parent()
    mother = Parent()

    son = Child()
    daughter = Child()

    # добавим отцу детей
    # children - колекция детей

    father.children.extend(son, daughter)

    # обратная ситуация - добавим сын и дочери маму (при двунаправленной связи)
    son.parents.append(mother)
    daughter.parents.append(mother)

    session.add(father)
    session.add(mother)
    session.add(son)
    session.add(daughter)
    session.commit()

    my_parents = session.query(Parent).all()
    my_children = session.query(Child).all()

    many_to_many_data = session.query(intergration_table).all()

    father.children.remove(daughter)
    # как себя поведет интеграциоооная таблица?
    # session.delete(son)

    print("for debug")
