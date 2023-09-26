import unittest
from number_in_interval import number_in_interval


class TestNumInInterval(unittest.TestCase):
    def test_number_within_interval(self):
        self.assertTrue(number_in_interval(50))

    def test_number_outside_interval(self):
        self.assertFalse(number_in_interval(190))
        self.assertFalse(number_in_interval(11))

    def test_number_is_25(self):
        self.assertFalse(number_in_interval(25))

    def test_number_is_100(self):
        self.assertFalse(number_in_interval(100))
