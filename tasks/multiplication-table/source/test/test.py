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


def expected_lines(num):
  return [f"{num} * {i} = {num * i}" for i in range(1, 11)]


class TestMultiplicationTable(unittest.TestCase):
  def test_asks_for_number(self):
    _, mock_input = run_main("5")
    mock_input.assert_called_once()

  def test_prints_ten_lines(self):
    out, _ = run_main("5")
    self.assertEqual(len(out.strip().splitlines()), 10)

  def test_table_of_five(self):
    out, _ = run_main("5")
    self.assertEqual(out.strip().splitlines(), expected_lines(5))

  def test_table_of_other_number(self):
    out, _ = run_main("7")
    self.assertEqual(out.strip().splitlines(), expected_lines(7))

  def test_table_of_zero(self):
    out, _ = run_main("0")
    self.assertEqual(out.strip().splitlines(), expected_lines(0))

  def test_negative_and_large_numbers(self):
    for value in (-3, 123456):
      out, _ = run_main(str(value))
      self.assertEqual(out.strip().splitlines(), expected_lines(value))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
