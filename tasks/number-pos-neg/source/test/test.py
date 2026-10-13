import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch

POSITIVE = "A szám pozitív"
NEGATIVE = "A szám negatív"
ZERO = "A szám nulla"


def run_main(value):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=value) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


def assert_only(test, out, expected):
  for message in (POSITIVE, NEGATIVE, ZERO):
    if message == expected:
      test.assertIn(message, out)
    else:
      test.assertNotIn(message, out)


class TestNumberPosNeg(unittest.TestCase):
  def test_asks_for_number(self):
    _, mock_input = run_main("5")
    mock_input.assert_called_once()

  def test_positive_number(self):
    out, _ = run_main("5")
    assert_only(self, out, POSITIVE)

  def test_negative_number(self):
    out, _ = run_main("-5")
    assert_only(self, out, NEGATIVE)

  def test_zero(self):
    out, _ = run_main("0")
    assert_only(self, out, ZERO)

  def test_boundary_values(self):
    out, _ = run_main("1")
    assert_only(self, out, POSITIVE)
    out, _ = run_main("-1")
    assert_only(self, out, NEGATIVE)

  def test_large_numbers(self):
    out, _ = run_main("1000000000")
    assert_only(self, out, POSITIVE)
    out, _ = run_main("-1000000000")
    assert_only(self, out, NEGATIVE)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
