#Pick your solution to one of the exercises in this module. Design tests for this solution and write tests using unittest library.

from ur8_tested_file import make_operation as tested
import unittest

class Testing(unittest.TestCase):
    def test_operand(self):
        with self.assertRaises(ValueError):
            tested('^', 4, 5)
        self.assertEqual(9, tested('+', 4, 5))
        self.assertEqual(-9, tested('-', 5, 4))
        self.assertEqual(20, tested('*', 4, 5))

    def test_negatives(self):
        self.assertEqual(-9, tested('+', -5, -4))
        self.assertEqual(9, tested('-', -5, -4))
        self.assertEqual(20, tested('*', -5, -4))
        self.assertEqual(-20, tested('*', -5, 4))


if __name__ == '__main__':
    unittest.main()