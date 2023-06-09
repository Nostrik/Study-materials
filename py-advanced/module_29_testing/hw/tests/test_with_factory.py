from .factories import ClientFactory, ParkingFactory
from ..main.models import Client, Parking


def test_create_client(app, db):
    client = ClientFactory()
    db.session.commit()
    assert client.id is not None
    assert len(db.session.query(Client).all()) == 1


def test_create_parking(client, db):
    parking = ParkingFactory()
    db.session.commit()
    assert parking.id is not None
    assert len(db.session.query(Parking).all()) == 1
