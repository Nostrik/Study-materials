import json
import pytest
from ..main.models import Client, Parking, ClientParking
from loguru import logger


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


def test_parking_entrance(client) -> None:
    parking_zone_data = {"address": "test_address", "opened": False,
                         "count_places": 10, "count_available_places": 0}
    client.post("/parkings", data=parking_zone_data)
    parking_data = {"parking_id": 2, "client_id": 2}
    response = client.post("/client_parkings", data=parking_data)
    assert response.status_code == 400
    assert response.text == 'This parking is not available'


def test_exit_from_the_parking_lot(client) -> None:
    parking_data = {"client_id": 1, "parking_id": 1}
