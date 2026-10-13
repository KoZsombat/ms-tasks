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
  return re.findall(r'-?\d+', text)


class TestTotalCost(unittest.TestCase):
  def test_asks_for_three_prices(self):
    _, mock_input = run_main("10", "20", "30")
    self.assertEqual(mock_input.call_count, 3)

  def test_calculates_total(self):
    out, _ = run_main("10", "20", "30")
    self.assertIn("60", numbers(out))

  def test_different_prices(self):
    out, _ = run_main("199", "250", "1000")
    self.assertIn("1449", numbers(out))

  def test_zero_prices(self):
    out, _ = run_main("0", "0", "0")
    self.assertIn("0", numbers(out))

  def test_equal_prices(self):
    out, _ = run_main("500", "500", "500")
    self.assertIn("1500", numbers(out))

  def test_large_prices(self):
    out, _ = run_main("1000000", "2000000", "3000000")
    self.assertIn("6000000", numbers(out))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
