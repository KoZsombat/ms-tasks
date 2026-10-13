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


def printed_numbers(value):
  out, _ = run_main(value)
  return [int(line) for line in out.strip().splitlines()]


class TestDivisibleNumbers(unittest.TestCase):
  def test_asks_for_divisor(self):
    _, mock_input = run_main("7")
    mock_input.assert_called_once()

  def test_multiples_of_seven(self):
    self.assertEqual(printed_numbers("7"), list(range(7, 101, 7)))

  def test_multiples_of_ten(self):
    self.assertEqual(printed_numbers("10"), list(range(10, 101, 10)))

  def test_divisor_one_prints_everything(self):
    self.assertEqual(printed_numbers("1"), list(range(1, 101)))

  def test_hundred_is_included(self):
    self.assertEqual(printed_numbers("100"), [100])

  def test_divisor_above_hundred_prints_nothing(self):
    out, _ = run_main("101")
    self.assertEqual(out.strip(), "")


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
