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


def expected_lines(rows):
  return [" " * (rows - i) + "*" * (2 * i - 1) for i in range(1, rows + 1)]


class TestStarPyramid(unittest.TestCase):
  def test_asks_for_rows(self):
    _, mock_input = run_main("4")
    mock_input.assert_called_once()

  def test_prints_requested_number_of_lines(self):
    out, _ = run_main("6")
    self.assertEqual(len(out.splitlines()), 6)

  def test_pyramid_of_four(self):
    out, _ = run_main("4")
    self.assertEqual(out.splitlines(), expected_lines(4))

  def test_pyramid_of_one(self):
    out, _ = run_main("1")
    self.assertEqual(out.splitlines(), ["*"])

  def test_larger_pyramid(self):
    out, _ = run_main("12")
    self.assertEqual(out.splitlines(), expected_lines(12))

  def test_zero_rows_prints_nothing(self):
    out, _ = run_main("0")
    self.assertEqual(out.strip(), "")


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
