from .app import db
from typing import Dict, Any


class Client(db.Model):
    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    credit_card = db.Column(db.String(50))
    car_number = db.Column(db.String(10))

    def __repr__(self):
        return f"Client {self.name}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class Parking(db.Model):
    __tablename__ = 'parking'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100), nullable=False)
    opened = db.Column(db.Boolean)
    count_places = db.Column(db.Integer, nullable=False)
    count_available_places = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Parking {self.id}, address {self.address}, " \
               f"opened {self.opened}, cnt_places {self.count_places}, " \
               f"cnt_available_places {self.count_available_places}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


class ClientParking(db.Model):
    __tablename__ = 'client_parking'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer)
    parking_id = db.Column(db.Integer)
    time_in = db.Column(db.DateTime)
    time_out = db.Column(db.DateTime)

    client = db.relationship("Client", backref="parkings")
    parking = db.relationship("Parking", backref="clients")

    def __repr__(self):
        return f"Client_Parking {self.id}, client_id {self.client_id}, parking_id {self.parking_id}" \
               f"time in {self.time_in}, time_out {self.time_out}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}
