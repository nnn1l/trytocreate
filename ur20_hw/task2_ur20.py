#Design tests for this solution and write tests using unittest library
import unittest
from ur20_hw.phonebook import *

class PhoneBook(unittest.TestCase):
    def test_new_entry(self):
        expected_result = 'Raiden'
        actual_result = new_entry('0682874625', 'Raiden', 'Shogun', 'Inazuma')
        self.assertEqual(expected_result, actual_result)

    def test_search(self):
        new_entry('0682874625', 'Raiden', 'Shogun', 'Inazuma')
        expected_result = 'Raiden', 'Shogun', '0682874625'
        actual_result = search('last name', 'Shogun')
        self.assertEqual(expected_result, actual_result)

    def test_delete(self):
        new_entry('0682874625', 'Raiden', 'Shogun', 'Inazuma')
        new_entry('0669993015', 'San', 'Fran', 'Poena')
        deleted = '0682874625'
        delete_record(deleted)
        self.assertNotIn(deleted, phonebook)

    def test_update(self):
        old = phonebook['0669993015']['first_name'], phonebook['0669993015']['last_name']
        update_record('0669993015', 'Timati', 'Walk', 'USA')
        new = phonebook['0669993015']['first_name'], phonebook['0669993015']['last_name']
        self.assertNotEqual(old, new)


if __name__ == '__main__':
    unittest.main()