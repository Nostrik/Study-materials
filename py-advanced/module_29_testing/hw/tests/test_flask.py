import pytest
from ..main.models import Parking, ClientParking
from datetime import datetime, timedelta


def test_get_all_clients(client) -> None:
    response = client.get("/clients")
    assert response.status_code == 200


def test_get_client_by_id(client) -> None:
    response = client.get("/clients/1")
    assert response.status_code == 200


@pytest.mark.parametrize("route", ["/clients", "/clients/1"])
def test_all_get_routes(client, route):
    response = client.get(route)
    assert response.status_code == 200


def test_create_new_client(client) -> None:
    client_data = {"name": "test_name", "surname": "test_surname",
                   "credit_card": "9090 0808"}
    response = client.post("/clients", data=client_data)
    assert response.status_code == 201


def test_create_new_parking_zone(client) -> None:
    parking_zone_data = {"address": "test_address", "opened": True,
                         "count_places": 10, "count_available_places": 10}
    response = client.post("/parkings", data=parking_zone_data)
    assert response.status_code == 201


@pytest.mark.parking
def test_parking_entrance(client) -> None:
    parking_zone_data = {"address": "test_address", "opened": False,
                         "count_places": 10, "count_available_places": 0}
    client.post("/parkings", data=parking_zone_data)
    parking_data = {"parking_id": 2, "client_id": 2}
    response = client.post("/client_parkings", data=parking_data)
    assert response.status_code == 400
    assert response.text == 'This parking is not available'


@pytest.mark.parking
def test_exit_from_the_parking_lot_no_credit_card(client) -> None:
    client_data = {"name": "test_name", "surname": "test_surname"}
    client.post("/clients", data=client_data)
    data_for_request = {"client_id": 2, "parking_id": 1}
    response = client.delete("/client_parkings", data=data_for_request)
    assert response.status_code == 500
    assert response.text == 'credit card not linked'


@pytest.mark.parking
def test_exit_from_the_parking_lot_time_problem(client, db) -> None:
    client_data = {"name": "test_name", "surname": "test_surname",
                   "credit_card": "9090 0808"}
    client.post("/clients", data=client_data)

    test_bad_time = ClientParking(
        client_id=1,
        parking_id=1,
        time_in=datetime.now() + timedelta(hours=2)
    )
    db.session.add(test_bad_time)
    db.session.commit()

    response = client.delete("/client_parkings", data={"client_id": 1, "parking_id": 1})
    assert response.status_code == 500
    assert response.text == 'parking time error'


@pytest.mark.parking
def test_exit_from_the_parking_lot_cnt_available_places(client, db):
    client_data = {"name": "test_name", "surname": "test_surname",
                   "credit_card": "9090 0808"}
    client.post("/clients", data=client_data)

    parking_zone_data = {"address": "test_address", "opened": True,
                         "count_places": 10, "count_available_places": 10}
    client.post("/parkings", data=parking_zone_data)

    parking_enter_data = {"parking_id": 1, "client_id": 1}
    client.post("/client_parkings", data=parking_enter_data)

    check_db_parking_note = db.session.query(Parking).get(1)
    assert check_db_parking_note.count_available_places == 9

    parking_exit_data = {"client_id": 1, "parking_id": 1}
    client.delete("/client_parkings", data=parking_exit_data)

    check_db_parking_note = db.session.query(Parking).get(1)
    assert check_db_parking_note.count_available_places == 10
