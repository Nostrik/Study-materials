import unittest
import datetime
from module_03_ci_culture_beginning.homework import person


class TestPerson(unittest.TestCase):

    def test_get_age(self):
        current_date = datetime.datetime.now()
        test_person = person.Person('test_name', 1990, 'test_street')
        test_person.get_age()

