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
  return [float(n) for n in re.findall(r'-?\d+(?:\.\d+)?', text)]


class TestInterest(unittest.TestCase):
  def test_asks_for_three_values(self):
    _, mock_input = run_main("1000", "5", "3")
    self.assertEqual(mock_input.call_count, 3)

  def test_calculates_interest(self):
    out, _ = run_main("1000", "5", "3")
    self.assertIn(150.0, numbers(out))

  def test_fractional_interest(self):
    out, _ = run_main("1000", "3", "1")
    self.assertIn(30.0, numbers(out))
    out, _ = run_main("150", "5", "1")
    self.assertIn(7.5, numbers(out))

  def test_zero_time(self):
    out, _ = run_main("1000", "5", "0")
    self.assertIn(0.0, numbers(out))

  def test_zero_rate(self):
    out, _ = run_main("1000", "0", "3")
    self.assertIn(0.0, numbers(out))

  def test_large_numbers(self):
    out, _ = run_main("1000000", "10", "10")
    self.assertIn(1000000.0, numbers(out))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
