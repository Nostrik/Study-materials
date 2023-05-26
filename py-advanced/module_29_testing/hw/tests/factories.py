import factory
import random
import factory.fuzzy as fuzzy
from ..main.models import Client, Parking
from ..main.app import db


class ClientFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Client
        sqlalchemy_session = db.session

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    credit_card = factory.LazyAttribute(lambda x: random.choice(['4444 8888', None]))
    car_number = fuzzy.FuzzyText()


class ParkingFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Parking
        sqlalchemy_session = db.session

    address = factory.Faker('street_address')
    opened = factory.Faker('boolean')
    count_places = factory.Faker('random_int', min=0, max=10)
    count_available_places = factory.Faker('random_int', min=0, max=count_places)
