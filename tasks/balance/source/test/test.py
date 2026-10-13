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


class TestBalance(unittest.TestCase):
  def test_asks_until_zero(self):
    _, mock_input = run_main("1000", "300", "200", "0")
    self.assertEqual(mock_input.call_count, 4)

  def test_several_expenses(self):
    out, _ = run_main("1000", "300", "200", "0")
    self.assertIn("500", numbers(out))

  def test_single_expense(self):
    out, _ = run_main("1000", "300", "0")
    self.assertIn("700", numbers(out))

  def test_no_expense(self):
    out, _ = run_main("800", "0")
    self.assertIn("800", numbers(out))

  def test_spent_more_than_earned(self):
    out, _ = run_main("100", "60", "90", "0")
    self.assertIn("-50", numbers(out))

  def test_large_numbers(self):
    out, _ = run_main("5000000", "1234567", "1000000", "0")
    self.assertIn("2765433", numbers(out))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
