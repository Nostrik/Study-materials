import unittest
import datetime
from module_03_ci_culture_beginning.homework.person import Person


class TestPerson(unittest.TestCase):
    def setUp(self) -> None:
        self.current_date = datetime.datetime.now()
        self.test_person = Person('test_name', 1990, 'test_street')

    def test_get_age(self):
        response = self.test_person.get_age()
        self.assertEqual(response, self.current_date.year)

    def test_get_name(self):
        self.assertEqual(self.test_person.get_name(), 'test_name')

    def test_set_name(self):
        self.test_person.set_name('anon')
        self.assertEqual(self.test_person.name, 'anon')

    def test_set_address(self):
        self.test_person.set_address('Wall Street')
        self.assertEqual(self.test_person.address, 'Wall Street')

    def test_get_address(self):
        self.test_person.address = 'test str'
        self.assertEqual(self.test_person.get_address(), 'test str')

    def test_is_homeless(self):
        test_homeless = self.test_person.is_homeless()
        if self.test_person.address is None:
            self.assertIsNone(test_homeless)
        else:
            self.assertFalse(test_homeless)


if __name__ == '__main__':
    unittest.main()
