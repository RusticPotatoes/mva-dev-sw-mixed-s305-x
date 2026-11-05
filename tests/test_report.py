import unittest

from sumbook.report import summary


class Report(unittest.TestCase):
    def test_summary(self):
        self.assertEqual(summary(["1.00", "2.50"]), "2 entries, total $3.50")

    def test_comments_and_blank_lines_are_skipped(self):
        self.assertEqual(summary(["# March", "", "4.00"]), "1 entries, total $4.00")
