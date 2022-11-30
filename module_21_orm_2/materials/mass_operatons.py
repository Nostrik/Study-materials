from sqlalchemy import Column, Integer, ForeignKey, create_engine, Table
from sqlalchemy.orm import relationship, sessionmaker, backref, joinedload
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mass_operations.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    # bulk_save_objects
    parent_1 = Parent(name="Nikita")
    parent_2 = Parent(name="Nastya")
    parent_3 = Parent(name="Vlad")
    parent_4 = Parent(name="Lera")

    session.bulk_save_objects([parent_1, parent_2, parent_3, parent_4])
    session.commit()

    parents = session.query(Parent).all()

    # bulk_inserts_mappings
    inserts_parents = [
        {"name": "Nikita2"},
        {"name": "Nastya2"},
        {"name": "Vlad2"},
        {"name": "Lera2"},
    ]
    session.bulk_insert_mappings(Parent, inserts_parents)
    session.commit()

    # bulk_update_mappings
    update_parents = [
        {"id": 1, "name": "Nikita_new"},
        {"id": 2, "name": "Nastya_new"},
    ]

    session.bulk_update_mappings(Parent, update_parents)
    session.commit()
    parents2 = session.query(Parent).all()

    print('end')
