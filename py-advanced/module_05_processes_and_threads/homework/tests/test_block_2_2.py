import unittest
import sys
from io import StringIO
from module_05_processes_and_threads.homework.block_2_2 import MyManager


class TestMyManager(unittest.TestCase):

    def setUp(self) -> None:
        self.test_exceptions = (ValueError, AttributeError)
        self.test_manager = MyManager('../test_input.txt', 'r', self.test_exceptions)

    def test_without_exceptions(self):
        with self.test_manager as file:
            s = file.read()
        self.assertTrue('input line 1' in s)
        self.assertTrue('input line 2' in s)
        self.assertTrue('input line 3' in s)

    def test_with_ValueError(self):
        with self.test_manager as file:
            s = file.read()
            raise FileNotFoundError
        temp_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        sys.stdout = temp_stdout
        result_str = result.getvalue()
        print('result_str: ', result_str)
        self.assertRaises(FileNotFoundError)
        self.assertTrue('FileNotFoundError' in result_str)



