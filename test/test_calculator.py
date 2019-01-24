# TODO Create test case for calculator
import unittest

from calculator import div


class TestCalculator(unittest.TestCase):
    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(-6, 6), -1)
        self.assertEqual(div(-8, -4), 2)

    def test_zero(self):
        self.assertRaises(ZeroDivisionError, div, 1, 0)

    def test_not_number(self):
        self.assertRaises(TypeError, div, 'a', 'b')


if __name__ == '__main__':
    unittest.main()
