import time
import typing as tp
import requests
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('[clients]')


class ApiClient:

    BOOKS_URL = 'http://127.0.0.1:5000/api/books'
    AUTHORS_URL = 'http://127.0.0.1:5000/api/authors'
    TIMEOUT = 5

    def __init__(self):
        self._session = requests.Session()

    def get_all_books(self) -> tp.Dict:
        response = self._session.get(f'{self.BOOKS_URL}', timeout=self.TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError('Error. Response message: {}'.format(response.json()))

    def get_all_authors(self) -> tp.Dict:
        response = self._session.get(f'{self.AUTHORS_URL}', timeout=self.TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError('Error. Response message: {}'.format(response.json()))


class ApiClientWithoutSession:

    BOOKS_URL = 'http://127.0.0.1:5000/api/books'
    AUTHORS_URL = 'http://127.0.0.1:5000/api/authors'
    TIMEOUT = 5

    def get_all_books(self) -> tp.Dict:
        response = requests.get(f'{self.BOOKS_URL}', timeout=self.TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError('Error. Response message: {}'.format(response.json()))

    def get_all_authors(self) -> tp.Dict:
        response = requests.get(f'{self.AUTHORS_URL}', timeout=self.TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError('Error. Response message: {}'.format(response.json()))


if __name__ == '__main__':
    client = ApiClient()
    conventional_client = ApiClientWithoutSession()

    start_1 = time.time()
    for _ in range(10):
        res = client.get_all_books()
        res2 = client.get_all_authors()
    logger.info(f'Ended in {time.time() - start_1}')

    start_2 = time.time()
    for _ in range(10):
        res = conventional_client.get_all_books()
        res2 = conventional_client.get_all_authors()
    logger.info(f'Ended in {time.time() - start_1}')
