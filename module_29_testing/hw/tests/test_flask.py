import json
import pytest
from ..main.models import Client, Parking, ClientParking


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


def test_parking_entrance(client, db) -> None:
    a = db.session.query(Parking).get(1)
    test_cur_parking_data = {"parking_id": 1}
    response = client.post("/client_parkings", data=test_cur_parking_data)
    assert response.status_code == 201
