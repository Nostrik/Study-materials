import unittest
from module_07_logging_part_2.homework.task_8_server import app
from module_07_logging_part_2.homework.task_8_handler import main


class TestLogHandler(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = True
        self.app_server = app.test_client()
        self.base_url = '/log-entry'

    def test_server_if_send_simple_msg(self):
        simple_msg = 'simple message'
        response = self.app_server.post(self.base_url, data={"msg": simple_msg})
        code = response.status_code
        response_text = response.data.decode()
        self.assertTrue(simple_msg in response_text)

    def test_handler(self):
        run_handler = main(0)
        pass
