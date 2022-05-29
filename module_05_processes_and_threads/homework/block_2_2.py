import unittest


class MyManager:
    def __init__(self, path: str, mode, ex_list):
        self.name = path
        self.mode = mode
        self.exceptions = ex_list

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            print('Exception was skipped')
            return True
        print("Exception {} has been handled".format(exc_type))
        self.file.close()


class ErrorManager:
    def __init__(self, errors: tuple):
        self.errors_list = errors

    def __enter__(self):
        print('Starting to calculate')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type and exc_type.__name__ in self.errors_list:
            print('Exception {} has been handled'.format(exc_type.__name__))
            return True


class TestErrorManager(unittest.TestCase):

    def test_error_manager(self):
        with ErrorManager(('IndexError', 'TypeError')):
            a = 1 + 2
        self.assertTrue(a == 3)

        with self.assertRaises(ZeroDivisionError):
            with ErrorManager(('IndexError', 'TypeError')):
                10 * (1 / 0)

        b = None
        with ErrorManager(('IndexError', 'TypeError')):
            b = 'sdf' + 2 + 5
        with ErrorManager(('IndexError', 'TypeError')):
            b = [1, 2][2]
        self.assertIsNone(b)


if __name__ == '__main__':
    ignore_exceptions = (ValueError, AttributeError)
    with MyManager('test_input.txt', 'r', ignore_exceptions) as file:
        s = file.read()
        print(s)
        raise ValueError
