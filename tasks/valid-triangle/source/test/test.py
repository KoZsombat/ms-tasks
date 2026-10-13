import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch

VALID = "Valódi háromszög"
INVALID = "Nem valódi háromszög"


def run_main(*values):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', side_effect=list(values)) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue().strip(), mock_input


class TestValidTriangle(unittest.TestCase):
  def check_sides(self, expected, *sides_list):
    for sides in sides_list:
      out, _ = run_main(*sides)
      self.assertEqual(out, expected, f"sides {sides}")

  def test_asks_for_three_sides(self):
    _, mock_input = run_main("3", "4", "5")
    self.assertEqual(mock_input.call_count, 3)

  def test_valid_triangle(self):
    self.check_sides(VALID, ("3", "4", "5"), ("5", "5", "5"), ("7", "10", "5"))

  def test_one_side_too_long(self):
    self.check_sides(INVALID, ("1", "1", "5"), ("10", "2", "3"), ("2", "20", "3"))

  def test_degenerate_triangle(self):
    self.check_sides(INVALID, ("1", "2", "3"), ("3", "1", "2"), ("2", "3", "1"))

  def test_side_order_does_not_matter(self):
    self.check_sides(VALID, ("3", "4", "5"), ("4", "5", "3"), ("5", "3", "4"))
    self.check_sides(INVALID, ("1", "1", "5"), ("1", "5", "1"), ("5", "1", "1"))

  def test_zero_side(self):
    self.check_sides(INVALID, ("0", "5", "5"), ("5", "0", "5"), ("5", "5", "0"))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
