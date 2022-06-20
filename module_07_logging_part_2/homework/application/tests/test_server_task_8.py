import unittest
from module_07_logging_part_2.homework.task_8_server import app


class TestLogHandler(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['WTF_CSRF_ENABLED'] = False
        self.app_server = app.test_client()
        self.base_url = '/log-entry'

    def test_get_success_request(self):
        response = self.app_server.post(self.base_url, data=dict(msg='test-msg'))
        with open('task_8_log_ser.log', mode='r') as log_file:
            text = log_file.read()
        response_code = response.status_code
        self.assertTrue('test-msg' in text)
        self.assertEqual(response_code, 200)
