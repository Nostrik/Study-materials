import json
import typing as tp
import requests
import logging
logging.basicConfig(level=logging.DEBUG)


class AuthorClient:

    URL = 'http://127.0.0.1:5000/api/authors'
    TIMEOUT = 5

    def __init__(self):
        self._session = requests.Session()

    def get_all_authors(self) -> tp.Dict:
        response = self._session.get(self.URL, timeout=self.TIMEOUT)
        return response.json()

    def add_new_author(self, data: tp.Dict):
        response = self._session.post(self.URL, json=data, timeout=self.TIMEOUT)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError('Wrong params. Response message: {}'.format(response.json()))


if __name__ == '__main__':
    a = AuthorClient()
    a._session.post(a.URL, data=json.dumps({'name': '1cl_tst_name', 'surname': '1cl_tst_surname'}),
                    headers={'content-type': 'application/json'})
