import io
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

from sumbook.cli import main


class Cli(unittest.TestCase):
    def test_prints_summary(self):
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "a.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write("1.25\n2.75\n")
            out = io.StringIO()
            with redirect_stdout(out):
                self.assertEqual(main([path]), 0)
            self.assertEqual(out.getvalue().strip(), "2 entries, total $4.00")

    def test_missing_file_exits_2(self):
        with redirect_stderr(io.StringIO()):
            self.assertEqual(main(["/nonexistent/amounts.txt"]), 2)
