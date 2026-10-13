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


class TestAvgSpeed(unittest.TestCase):
  def test_asks_for_distance_and_time(self):
    _, mock_input = run_main("120", "2")
    self.assertEqual(mock_input.call_count, 2)

  def test_calculates_speed(self):
    out, _ = run_main("120", "2")
    self.assertIn(60.0, numbers(out))

  def test_fractional_speed(self):
    out, _ = run_main("100", "8")
    self.assertIn(12.5, numbers(out))

  def test_one_hour(self):
    out, _ = run_main("50", "1")
    self.assertIn(50.0, numbers(out))

  def test_zero_distance(self):
    out, _ = run_main("0", "5")
    self.assertIn(0.0, numbers(out))

  def test_large_numbers(self):
    out, _ = run_main("1000000", "10")
    self.assertIn(100000.0, numbers(out))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
