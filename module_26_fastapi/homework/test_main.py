from fastapi.testclient import TestClient
from .main import app
from loguru import logger

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    logger.debug(response)
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_get_all_recipes():
    response = client.get('/recipe/')
    assert response.status_code == 200
