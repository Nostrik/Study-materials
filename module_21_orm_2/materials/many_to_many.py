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
