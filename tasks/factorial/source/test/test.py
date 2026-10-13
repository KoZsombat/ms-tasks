import contextlib
import importlib
import io
import math
import sys
import unittest
from unittest.mock import patch


def run_main(value):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=value) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


class TestFactorial(unittest.TestCase):
  def test_asks_for_number(self):
    _, mock_input = run_main("5")
    mock_input.assert_called_once()

  def test_factorial_of_five(self):
    out, _ = run_main("5")
    self.assertIn("120", out)

  def test_factorial_of_one(self):
    out, _ = run_main("1")
    self.assertIn("1", out)

  def test_factorial_of_other_number(self):
    out, _ = run_main("7")
    self.assertIn("5040", out)

  def test_factorial_of_large_number(self):
    out, _ = run_main("20")
    self.assertIn(str(math.factorial(20)), out)

  def test_factorial_of_zero(self):
    out, _ = run_main("0")
    self.assertIn("1", out)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
