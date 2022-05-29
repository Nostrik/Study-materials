import unittest
from module_05_processes_and_threads.homework.block_2_1 import *
from module_05_processes_and_threads.materials.prev_hw_review.hw_3_1 import app


class TestRunningFlaskApp(unittest.TestCase):
    def setUp(self) -> None:
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['PORT'] = 5000
        self.app = app.test_client()

    def test_use_lsof_command(self):
        result_block_2_1 = use_lsof_and_kill_proc()
        self.assertEqual(result_block_2_1, None)
