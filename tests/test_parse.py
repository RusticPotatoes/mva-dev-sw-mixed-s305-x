import unittest

from sumbook.parse import parse_amount


class Parse(unittest.TestCase):
    def test_plain(self):
        self.assertEqual(parse_amount("12.34"), 1234)

    def test_one_decimal_is_tens_of_cents(self):
        self.assertEqual(parse_amount("12.5"), 1250)

    def test_whole_and_negative(self):
        self.assertEqual(parse_amount("-3"), -300)
        self.assertEqual(parse_amount(" 7.25 "), 725)
