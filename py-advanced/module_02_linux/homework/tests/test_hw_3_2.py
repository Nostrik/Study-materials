import unittest
import random

from module_02_linux.homework.hw_3_2 import app


class TestFinanceApp(unittest.TestCase):
    storage = {
        '20000120': 10,
        '20000220': 20,
        '20000222': 30,
        '19990530': 40
    }
    not_valid_date = [
        '20100229',
        '21052020',
        '1999',
        ' ',
        '',
    ]

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_add_url = '/add/'
        self.base_calculate_url = '/calculate/'

    def test_calculate_year_storage_is_empty(self):
        response = self.app.get(self.base_calculate_url + '2002')
        response_text = response.data.decode()
        self.assertTrue('0' in response_text)

    def test_calculate_year_and_mounth_storage_is_empty(self):
        response = self.app.get(self.base_calculate_url + '2000/2')
        response_text = response.data.decode()
        self.assertTrue('0' in response_text)

    def test_add(self):
        response = self.app.get(self.base_add_url + '20020120/10')
        response_text = response.data.decode()
        self.assertTrue('Данные сохранены' in response_text)

    def test_add_can_get_not_valid_date(self):
        test_date = random.choice(self.not_valid_date)
        response = self.app.get(self.base_add_url + f'{test_date}/10')
        response_text = response.data.decode()
        self.assertTrue('Неверный формат даты!' in response_text)

    def test_calculate_year(self):
        for k, v in self.storage.items():
            test_response = self.app.get(self.base_add_url + f'{k}/{v}')
        response = self.app.get(self.base_calculate_url + '2000')
        response_text = response.data.decode()
        self.assertTrue('60' in response_text)

    def test_calculate_year_and_mounth(self):
        response = self.app.get(self.base_calculate_url + '2000/2')
        response_text = response.data.decode()
        self.assertTrue('50' in response_text)
