from sqlalchemy import Column, Integer, String, Boolean, JSON, ARRAY, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from typing import Dict, Any
from data_fake_request import start_download
# from ..data_app.app import start_download
Base = declarative_base()


class Coffee(Base):
    __tablename__ = 'coffee'
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String(200), nullable=False)
    origin = Column(String(200))
    intensifer = Column(String(100))
    notes = Column(ARRAY(item_type=String))

    def __repr__(self):
        return f"Coffee {self.title}"

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
        return f"User {self.username}"

    def to_json(self) -> Dict[str, Any]:
        return {c.name: getattr(self, c.name) for c in
                self.__table__.columns}


# objects = [
#     User(name='Clarisa', address={
#         "id": 1394,
#         "uid": "4909ac53-6056-46d8-a218-c0140de95e52",
#         "city": "Williamsonberg",
#         "street_name": "Berge Plains",
#         "street_address": "5891 Stanford Extensions",
#         "secondary_address": "Suite 480",
#         "building_number": "1606",
#         "mail_box": "PO Box 810",
#         "community": "Paradise Heights",
#         "zip_code": "51507",
#         "zip": "95293",
#         "postcode": "89665-4749",
#         "time_zone": "Australia/Melbourne",
#         "street_suffix": "Port",
#         "city_suffix": "mouth",
#         "city_prefix": "South",
#         "state": "Ohio",
#         "state_abbr": "MO",
#         "country": "Portugal",
#         "country_code": "CI",
#         "latitude": -31.519174918978273,
#         "longitude": -21.949730933607384,
#         "full_address": "74217 Schuppe Ford, Lake Rigoberto, NH 46439"
#     }),
#     User(name='Shanika', address={
#         "id": 6153,
#         "uid": "f6fb06c5-c6e7-4c97-b1ba-30e622df86dc",
#         "city": "North Napoleonville",
#         "street_name": "Lola Village",
#         "street_address": "359 Klein Valley",
#         "secondary_address": "Suite 586",
#         "building_number": "411",
#         "mail_box": "PO Box 9054",
#         "community": "Pine Court",
#         "zip_code": "27047-1902",
#         "zip": "21683-3326",
#         "postcode": "02734",
#         "time_zone": "America/Godthab",
#         "street_suffix": "Viaduct",
#         "city_suffix": "burgh",
#         "city_prefix": "North",
#         "state": "Florida",
#         "state_abbr": "IL",
#         "country": "Ghana",
#         "country_code": "NO",
#         "latitude": 73.46615133539484,
#         "longitude": -156.75886204438842,
#         "full_address": "Suite 829 813 Adrianna Trace, Krajcikport, MI 03712"
#     }),
#     User(name='Maribeth', address={
#         "id": 5298,
#         "uid": "0d4e3594-a5d8-4a31-8344-fdb4eac84d81",
#         "city": "Lake Hanafurt",
#         "street_name": "Vito Passage",
#         "street_address": "2974 Hackett Square",
#         "secondary_address": "Suite 686",
#         "building_number": "852",
#         "mail_box": "PO Box 139",
#         "community": "Willow Creek",
#         "zip_code": "76221",
#         "zip": "76511-8015",
#         "postcode": "86165",
#         "time_zone": "Europe/Skopje",
#         "street_suffix": "Freeway",
#         "city_suffix": "view",
#         "city_prefix": "South",
#         "state": "Rhode Island",
#         "state_abbr": "NJ",
#         "country": "Sudan",
#         "country_code": "AD",
#         "latitude": 5.464151769198168,
#         "longitude": -12.723409679300374,
#         "full_address": "Apt. 380 296 Hortencia Green, East Linwood, AZ 69656-3004"
#     }),
#     User(name='Jennell', address={
#         "id": 6040,
#         "uid": "9e1af759-acb8-4e4a-bae6-ab10057350e7",
#         "city": "Hansentown",
#         "street_name": "Marti Courts",
#         "street_address": "96387 Kertzmann Crescent",
#         "secondary_address": "Apt. 579",
#         "building_number": "10590",
#         "mail_box": "PO Box 82",
#         "community": "Willow Estates",
#         "zip_code": "62985-6277",
#         "zip": "39864-3613",
#         "postcode": "53127",
#         "time_zone": "America/Regina",
#         "street_suffix": "Oval",
#         "city_suffix": "view",
#         "city_prefix": "West",
#         "state": "Florida",
#         "state_abbr": "AL",
#         "country": "Malawi",
#         "country_code": "NF",
#         "latitude": -50.643908851235246,
#         "longitude": -132.364710956869,
#         "full_address": "80393 King Lodge, East Scottyland, RI 15743-9168"
#     }),
#     User(name='Thresa', address={
#         "id": 5577,
#         "uid": "d19033cd-adaa-487d-bff6-830f468aaef6",
#         "city": "Cordellberg",
#         "street_name": "Lavelle Cove",
#         "street_address": "5104 Ismael Pike",
#         "secondary_address": "Suite 556",
#         "building_number": "977",
#         "mail_box": "PO Box 100",
#         "community": "University Acres",
#         "zip_code": "10782",
#         "zip": "16993",
#         "postcode": "10496-3249",
#         "time_zone": "Europe/Lisbon",
#         "street_suffix": "Underpass",
#         "city_suffix": "ville",
#         "city_prefix": "West",
#         "state": "Oklahoma",
#         "state_abbr": "AL",
#         "country": "Paraguay",
#         "country_code": "SR",
#         "latitude": 60.49700997899032,
#         "longitude": 144.30394011478194,
#         "full_address": "Suite 671 2812 Cody Ridges, Lake Shanimouth, AL 82651-4005"
#     }),
#     User(name='Kristan', address={
#         "id": 8542,
#         "uid": "9448d60a-d811-4fb8-a596-d40cea4b80b4",
#         "city": "Gerlachville",
#         "street_name": "Art Well",
#         "street_address": "39679 Koss Curve",
#         "secondary_address": "Suite 433",
#         "building_number": "483",
#         "mail_box": "PO Box 2045",
#         "community": "Autumn Acres",
#         "zip_code": "36004",
#         "zip": "01855",
#         "postcode": "29219-5294",
#         "time_zone": "Pacific/Honolulu",
#         "street_suffix": "Tunnel",
#         "city_suffix": "berg",
#         "city_prefix": "New",
#         "state": "Oregon",
#         "state_abbr": "ME",
#         "country": "Bosnia and Herzegovina",
#         "country_code": "HU",
#         "latitude": -54.78380794569073,
#         "longitude": 34.59305604339906,
#         "full_address": "91442 Ardelle Orchard, New Leighabury, SD 36548-9324"
#     }),
#     User(name='Paris', address={
#         "id": 6967,
#         "uid": "e6c7b406-2df6-4f57-a558-5be9ef96af03",
#         "city": "Stehrville",
#         "street_name": "McDermott Villages",
#         "street_address": "373 Ethyl Ville",
#         "secondary_address": "Suite 113",
#         "building_number": "97822",
#         "mail_box": "PO Box 3311",
#         "community": "Park Square",
#         "zip_code": "75535-9915",
#         "zip": "35724",
#         "postcode": "99582-5442",
#         "time_zone": "America/Argentina/Buenos_Aires",
#         "street_suffix": "Road",
#         "city_suffix": "stad",
#         "city_prefix": "Lake",
#         "state": "Kentucky",
#         "state_abbr": "MO",
#         "country": "Seychelles",
#         "country_code": "IS",
#         "latitude": -86.21207271412568,
#         "longitude": -178.14511598845897,
#         "full_address": "498 Rachele Cape, East Leena, NC 82107-7924"
#     }),
#     User(name='Wilbert', address={
#         "id": 5026,
#         "uid": "350da8c8-fed9-43d1-bb09-34fd547556da",
#         "city": "South Noble",
#         "street_name": "Barton Station",
#         "street_address": "47000 Jame Fall",
#         "secondary_address": "Suite 741",
#         "building_number": "1624",
#         "mail_box": "PO Box 391",
#         "community": "University Oaks",
#         "zip_code": "23313",
#         "zip": "82031-3792",
#         "postcode": "32314",
#         "time_zone": "Europe/Helsinki",
#         "street_suffix": "Landing",
#         "city_suffix": "berg",
#         "city_prefix": "North",
#         "state": "Rhode Island",
#         "state_abbr": "MA",
#         "country": "Wallis and Futuna",
#         "country_code": "ES",
#         "latitude": 9.515447378519951,
#         "longitude": -0.4433546911513133,
#         "full_address": "5878 Wolff Mall, New Hobert, AZ 34703-3176"
#     }),
#     User(name='Maxwell', address={
#         "id": 8707,
#         "uid": "e112f7ca-115d-4031-a855-33a3b39d8ac0",
#         "city": "North Theodore",
#         "street_name": "Gleason Spring",
#         "street_address": "580 Hamill Curve",
#         "secondary_address": "Apt. 549",
#         "building_number": "4688",
#         "mail_box": "PO Box 57",
#         "community": "Royal Village",
#         "zip_code": "43152",
#         "zip": "44907",
#         "postcode": "89834-0199",
#         "time_zone": "Pacific/Tongatapu",
#         "street_suffix": "Squares",
#         "city_suffix": "land",
#         "city_prefix": "Port",
#         "state": "Washington",
#         "state_abbr": "MD",
#         "country": "United Arab Emirates",
#         "country_code": "RU",
#         "latitude": -58.715804863985966,
#         "longitude": -174.8825150333866,
#         "full_address": "3929 Carmelo Dam, Cecilton, MI 84086"
#     }),
#     User(name='Fidel', address={
#         "id": 872,
#         "uid": "83dac139-718c-4176-b32b-26381250e842",
#         "city": "Lake Eugeneview",
#         "street_name": "Irvin Radial",
#         "street_address": "4074 Howard Ridge",
#         "secondary_address": "Suite 949",
#         "building_number": "7467",
#         "mail_box": "PO Box 7753",
#         "community": "Autumn Crossing",
#         "zip_code": "97938-0969",
#         "zip": "40113",
#         "postcode": "71360",
#         "time_zone": "Pacific/Guam",
#         "street_suffix": "Estate",
#         "city_suffix": "mouth",
#         "city_prefix": "East",
#         "state": "New Mexico",
#         "state_abbr": "OR",
#         "country": "Western Sahara",
#         "country_code": "GS",
#         "latitude": -36.14586474561316,
#         "longitude": 176.45542943379542,
#         "full_address": "Apt. 783 664 Chery Union, Daniellechester, AR 08060-7469"
#     }),
#     Coffee(title='Street Cup', notes='sharp, slick, red currant, walnut, raspberry'),
#     Coffee(title='Strong Extract', notes='clean, smooth, rose hips, cedar, kiwi'),
#     Coffee(title='Blue Look', notes='sharp, big, green apple, butter, black cherry'),
#     Coffee(title='Melty Breaker', notes='rounded, velvety, burnt sugar, plum, sweet pea'),
#     Coffee(title='Café Forrester', notes='vibrant, tea-like, lemon verbena, black currant, sage'),
#     Coffee(title='Postmodern Light', notes='balanced, chewy, plum, sage, peach'),
#     Coffee(title='Kreb-Full-o Star', notes='unbalanced, coating, lychee, mango, wheat'),
#     Coffee(title='The Captain Extract', notes='clean, full, lychee, red grape, cream'),
#     Coffee(title='Veranda Mug', notes='mild, creamy, orange creamsicle, watermelon, fresh bread'),
#     Coffee(title='American Delight', notes='structured, velvety, clementine, toast, carbon'),
# ]

user_obj_list, coffee_obj_list = start_download()
user_objects = [User(name=user_obj_list[i]['first_name'], address=user_obj_list[i]['address']) for i in range(0, 10)]
coffee_objects = [Coffee(title=coffee_obj_list[i]['blend_name'], notes=coffee_obj_list[i]['notes']) for i in range(0, 10)]
