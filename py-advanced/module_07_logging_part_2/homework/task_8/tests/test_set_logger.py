import unittest

from module_07_logging_part_2.homework.get_logs_task_8.set_logger_api import app


class TestSetLoggerApi(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["WTF_CSRF_ENABLED"] = False
        self.app = app.test_client()

    def test_get_success_requests(self):
        response = self.app.post(
            '/set_log_info',
            data=dict(
                message='test-error',
            )
        )
        response_code = response.status_code
        with open('log.log', mode='r') as f:
            m = f.read()
        self.assertTrue('test-error' in m)
        self.assertEqual(response_code, 200)
