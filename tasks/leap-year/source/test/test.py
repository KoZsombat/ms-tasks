import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch

LEAP = "Szökő év"
COMMON = "Nincs szökő év"


def run_main(value):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=value) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue().strip(), mock_input


class TestLeapYear(unittest.TestCase):
  def check_years(self, expected, years):
    for year in years:
      out, _ = run_main(year)
      self.assertEqual(out, expected, f"year {year}")

  def test_asks_for_year(self):
    _, mock_input = run_main("2024")
    mock_input.assert_called_once()

  def test_leap_year(self):
    self.check_years(LEAP, ["2024", "2028", "1996"])

  def test_common_year(self):
    self.check_years(COMMON, ["2023", "2025", "2026"])

  def test_century_is_not_leap_year(self):
    self.check_years(COMMON, ["1900", "2100", "1800"])

  def test_divisible_by_400_is_leap_year(self):
    self.check_years(LEAP, ["2000", "1600", "2400"])


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
