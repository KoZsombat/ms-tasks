import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch

COAT = "Kabátot vegyél fel"
SWEATER = "Pulcsit vegyél fel"
TSHIRT = "Póló elég"


def run_main(value):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=value) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


def assert_only(test, out, expected):
  for message in (COAT, SWEATER, TSHIRT):
    if message == expected:
      test.assertIn(message, out)
    else:
      test.assertNotIn(message, out)


class TestSuitableClothing(unittest.TestCase):
  def test_asks_for_temperature(self):
    _, mock_input = run_main("15")
    mock_input.assert_called_once()

  def test_cold_weather(self):
    for value in ("5", "-10"):
      out, _ = run_main(value)
      assert_only(self, out, COAT)

  def test_mild_weather(self):
    out, _ = run_main("15")
    assert_only(self, out, SWEATER)

  def test_warm_weather(self):
    out, _ = run_main("25")
    assert_only(self, out, TSHIRT)

  def test_boundary_ten(self):
    out, _ = run_main("9")
    assert_only(self, out, COAT)
    out, _ = run_main("10")
    assert_only(self, out, SWEATER)

  def test_boundary_twenty(self):
    out, _ = run_main("19")
    assert_only(self, out, SWEATER)
    out, _ = run_main("20")
    assert_only(self, out, TSHIRT)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
