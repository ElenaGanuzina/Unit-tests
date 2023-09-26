import unittest
from even_odd_num import even_odd_number


class TestEvenOddNumber(unittest.TestCase):
    def test_ever_number(self):
        self.assertTrue(even_odd_number(8))

    def test_odd_number(self):
        self.assertFalse(even_odd_number(11))


