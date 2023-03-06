from sqlalchemy import Column, Integer, String, Boolean, JSON, ARRAY, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from typing import Dict, Any
from data_fake_request import start_download
from pprint import pprint
Base = declarative_base()


class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String(200), nullable=False)
    origin = Column(String(200))
    intensifier = Column(String(100))
    notes = Column(ARRAY(item_type=String))
    user = relationship("User", backref="coffee")

    def __repr__(self):
        return f"Coffee {self.title}, notes {self.notes}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(20), nullable=False)
    has_sale = Column(Boolean)
    address = Column(JSON)
    coffee_id = Column(Integer, ForeignKey('coffee.id'))

    def __repr__(self):
        return f"User {self.name}, has_sale {self.has_sale}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


user_obj_list, coffee_obj_list = start_download()

objects = []
for i in range(10):
    row = User(name=user_obj_list[i]['first_name'], address=user_obj_list[i]['address'])
    objects.append(row)
for i in range(10):
    notes_list = []
    for i_note in coffee_obj_list[i]['notes'].split(','):
        notes_list.append(i_note)
    row = Coffee(title=coffee_obj_list[i]['blend_name'], notes=notes_list)
    objects.append(row)
