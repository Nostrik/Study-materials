"""
Для каждого поля и валидатора в endpoint /registration напишите по unit-тесту,
    который проверит, что валидатор и правда работает (т.е. мы должны проверить,
    что существует набор данных, которые проходят валидацию, и такие,
    которые валидацию не проходят)
"""
import copy
import unittest
from module_04_flask.hw.hw_1_2 import app


class TestRegistrationValid(unittest.TestCase):
    test_information = {
        "email": "test@example.com",
        "phone": 89606212121,
        "name": "Иванов Иван",
        "address": "На деревне, дедушке",
        "index": 183900,
        "comment": "Вход со двора"
    }

    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()
        self.base_url = '/registration'

    def test_all_info_valid(self):
        response = self.app.post(self.base_url, data=self.test_information)
        response_text = response.data.decode()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(f"Successfully registered user {self.test_information['email']} "
                        f"with phone +7{self.test_information['phone']}" in response_text)

    def test_email_valid(self):
        test_email_valid_info = copy.deepcopy(self.test_information)

        test_email_valid_info["email"] = ""
        response = self.app.post(self.base_url, data=test_email_valid_info)
        response_text = response.data.decode()
        self.assertTrue('This field is required.' in response_text)

        test_email_valid_info["email"] = "testexample.com"
        response = self.app.post(self.base_url, data=test_email_valid_info)
        response_text = response.data.decode()
        self.assertTrue('Invalid email address' in response_text)

        test_email_valid_info["email"] = "test@examplecom"
        response = self.app.post(self.base_url, data=test_email_valid_info)
        response_text = response.data.decode()
        self.assertTrue('Invalid email address' in response_text)

        test_email_valid_info["email"] = "test@example."
        response = self.app.post(self.base_url, data=test_email_valid_info)
        response_text = response.data.decode()
        self.assertTrue('Invalid email address' in response_text)

    def test_phone_valid(self):
        test_phone_valid_info = copy.deepcopy(self.test_information)

        test_phone_valid_info["phone"] = 960621212111
        response = self.app.post(self.base_url, data=test_phone_valid_info)
        response_text = response.data.decode()
        self.assertTrue('Number must be between 1000000000 and 99999999999.' in response_text)

        test_phone_valid_info["phone"] = ""
        response = self.app.post(self.base_url, data=test_phone_valid_info)
        response_text = response.data.decode()
        self.assertTrue('This field is required.' in response_text)

    def test_name_valid(self):
        test_name_valid_info = copy.deepcopy(self.test_information)

        test_name_valid_info["name"] = ""
        response = self.app.post(self.base_url, data=test_name_valid_info)
        response_text = response.data.decode()
        self.assertTrue('This field is required.' in response_text)

    def test_address_valid(self):
        test_address_valid_info = copy.deepcopy(self.test_information)

        test_address_valid_info["address"] = ""
        response = self.app.post(self.base_url, data=test_address_valid_info)
        response_text = response.data.decode()
        self.assertTrue('This field is required.' in response_text)

    def test_index_valid(self):
        test_index_valid_info = copy.deepcopy(self.test_information)

        test_index_valid_info["index"] = "O"
        response = self.app.post(self.base_url, data=test_index_valid_info)
        response_text = response.data.decode()
        self.assertTrue('Not a valid integer value.' in response_text)
