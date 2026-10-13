import contextlib
import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch


def run_main(*values):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', side_effect=list(values)) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


def numbers(text):
  return re.findall(r'\d+', text)


class TestRectangleArea(unittest.TestCase):
  def test_asks_for_two_values(self):
    _, mock_input = run_main("3", "4")
    self.assertEqual(mock_input.call_count, 2)

  def test_calculates_area(self):
    out, _ = run_main("3", "4")
    self.assertIn("12", numbers(out))

  def test_different_values(self):
    out, _ = run_main("7", "5")
    self.assertIn("35", numbers(out))

  def test_square(self):
    out, _ = run_main("6", "6")
    self.assertIn("36", numbers(out))

  def test_zero_side(self):
    out, _ = run_main("0", "9")
    self.assertIn("0", numbers(out))

  def test_large_numbers(self):
    out, _ = run_main("123456", "1000")
    self.assertIn("123456000", numbers(out))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
