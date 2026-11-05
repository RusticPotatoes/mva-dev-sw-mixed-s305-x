import unittest

from sumbook.money import format_cents


class Money(unittest.TestCase):
    def test_whole_and_cents(self):
        self.assertEqual(format_cents(12345), "$123.45")

    def test_small_cents_keep_two_digits(self):
        self.assertEqual(format_cents(105), "$1.05")

    def test_negative(self):
        self.assertEqual(format_cents(-250), "-$2.50")
