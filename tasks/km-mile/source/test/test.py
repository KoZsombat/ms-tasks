import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main():
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value='') as mock_input, contextlib.redirect_stdout(out):
    module = importlib.import_module('main')
  return out.getvalue(), mock_input, module


class TestKmMile(unittest.TestCase):
  def assertClose(self, actual, expected):
    self.assertAlmostEqual(actual, expected, delta=max(abs(expected) * 0.01, 1e-9))

  def test_km_to_mile(self):
    _, _, main = run_main()
    self.assertClose(main.km_mile(1), 0.621)
    self.assertClose(main.km_mile(10), 6.214)

  def test_mile_to_km(self):
    _, _, main = run_main()
    self.assertClose(main.mile_km(1), 1.609)
    self.assertClose(main.mile_km(10), 16.09)

  def test_zero_distance(self):
    _, _, main = run_main()
    self.assertClose(main.km_mile(0), 0)
    self.assertClose(main.mile_km(0), 0)

  def test_decimal_distance(self):
    _, _, main = run_main()
    self.assertClose(main.km_mile(2.5), 1.553)
    self.assertClose(main.mile_km(0.5), 0.8045)

  def test_prints_results(self):
    out, _, main = run_main()
    self.assertIn(str(main.mile_km(1)), out)
    self.assertIn(str(main.km_mile(1)), out)

  def test_no_input(self):
    _, mock_input, _ = run_main()
    mock_input.assert_not_called()


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
