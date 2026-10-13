import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main(value):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=value) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


def is_reported_prime(value):
  out, _ = run_main(str(value))
  return out.strip() == "Prímszám"


def is_reported_not_prime(value):
  out, _ = run_main(str(value))
  return out.strip() == "Nem prímszám"


class TestPrimeCheck(unittest.TestCase):
  def test_asks_for_number(self):
    _, mock_input = run_main("7")
    mock_input.assert_called_once()

  def test_small_primes(self):
    for value in (2, 3, 5, 7, 13):
      self.assertTrue(is_reported_prime(value), value)

  def test_composite_numbers(self):
    for value in (4, 9, 15, 100):
      self.assertTrue(is_reported_not_prime(value), value)

  def test_one_is_not_prime(self):
    self.assertTrue(is_reported_not_prime(1))

  def test_zero_and_negative_are_not_prime(self):
    for value in (0, -7):
      self.assertTrue(is_reported_not_prime(value), value)

  def test_large_prime(self):
    self.assertTrue(is_reported_prime(7919))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
