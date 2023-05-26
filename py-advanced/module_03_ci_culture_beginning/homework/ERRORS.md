# test_person
## TestPerson
### test_get_address <+>
### test_get_age <->
ErrorTraceback (most recent call last):
File "C:\Users\FalevMV\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\tests\test_person.py", line 12, in test_get_age
response = self.test_person.get_age()
File "C:\Users\FalevMV\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\person.py", line 9, in get_age
now = datetime.datetime.now()
NameError: name 'datetime' is not defined
### test_get_name <+>
### test_is_homeles <->
ErrorTraceback (most recent call last):
File "C:\Users\FalevMV\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\tests\test_person.py", line 31, in test_is_homeless
test_homeless = self.test_person.is_homeless()
File "C:\Users\FalevMV\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\person.py", line 28, in is_homeless
return address is None
NameError: name 'address' is not defined
### test_set_address <->
Ran 6 tests in 0.016s
FAILED (failures=2, errors=2)
Wall Street != test_street
Traceback (most recent call last):
File "C:\Users\FalevMV\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\tests\test_person.py", line 24, in test_set_address
self.assertEqual(self.test_person.address, 'Wall Street')
AssertionError: 'test_street' != 'Wall Street'
/- test_street
/+ Wall Street
### test_set_name
anon != test_name
Traceback (most recent call last):
File "C:\Users\FalevMV\PycharmProjects\python_advanced\module_03_ci_culture_beginning\homework\tests\test_person.py", line 20, in test_set_name
self.assertEqual(self.test_person.name, 'anon')
AssertionError: 'test_name' != 'anon'
/- test_name
/+ anon
