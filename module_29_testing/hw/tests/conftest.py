import pytest
from flask import template_rendered
from ..main.app import create_app, db as _db
from ..main.models import Client, Parking, ClientParking
from datetime import datetime, timedelta


@pytest.fixture
def app():
    _app = create_app()
    _app.config["TESTING"] = True
    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with _app.app_context():
        _db.create_all()
        client = Client(
            id=1,
            name="name",
            surname="surname",
            credit_card="credit_card"
        )
        parking = Parking(
            id=1,
            address="address",
            opened=True,
            count_places=10,
            count_available_places=10
        )
        client_parking = ClientParking(
            id=1,
            client_id=1,
            parking_id=1,
            time_in=datetime.now(),
            time_out=datetime.now() + timedelta(hours=3)
        )
        _db.session.add(client)
        _db.session.add(parking)
        _db.session.add(client_parking)

        yield _app
        _db.session.close()
        _db.drop_all()


@pytest.fixture
def client(app):
    client = app.test_client()
    yield client
