import sys
import unittest
from typing import TextIO


class OutputManager:
    def __init__(self, io_obj1: TextIO, io_obj2):
        self.io_obj1 = io_obj1
        self.io_obj2 = io_obj2

    def __enter__(self):
        #  При входе в контекст нужно сохранять текущие
        #  значения sys.stdout и sys.stderr, а при выходе
        #  возвращать их в исxодное состояние.
        self.current_stdout, self.current_stderr = sys.stdout, sys.stderr
        sys.stdout, sys.stderr = self.io_obj1, self.io_obj2

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('Exception {} has been handled'.format(exc_type))
        sys.stdout, sys.stderr = self.current_stdout, self.current_stderr
        # Поток io_obj можно здесь не закрывать.
        return True


class TestOutputManager(unittest.TestCase):
    def setUp(self) -> None:
        file1 = open('file1.txt', 'w')
        file2 = open('file2.txt', 'w')
        with OutputManager(file1, file2):
            print('Print to stdout')
            print('Print to stderr', file=sys.stderr)
            10 * 1 / 0
        file1.close()
        file2.close()

    def test_output_manager(self):
        with open('file1.txt', 'r') as file:
            text = file.read()
        self.assertIn('Print to stdout', text)
        self.assertIn('ZeroDivisionError', text)

        with open('file2.txt', 'r') as file:
            text = file.read()
        self.assertIn('Print to stderr', text)


if __name__ == '__main__':
    file1 = open('file1.txt', 'w')
    file2 = open('file2.txt', 'w')
    with OutputManager(file1, file2):
        print('Print to stdout')
        print('Print to stderr', file=sys.stderr)
        10 * 1 / 0
    file1.close()
    file2.close()
