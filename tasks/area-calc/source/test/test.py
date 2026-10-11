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


class TestAreaCalc(unittest.TestCase):
  def test_rectangle_area(self):
    _, _, main = run_main()
    self.assertEqual(main.rectangle_area(2, 4), 8)
    self.assertEqual(main.rectangle_area(5, 3), 15)

  def test_triangle_area(self):
    _, _, main = run_main()
    self.assertEqual(main.triangle_area(2, 4), 4)
    self.assertEqual(main.triangle_area(6, 3), 9)

  def test_triangle_half_result(self):
    _, _, main = run_main()
    self.assertAlmostEqual(main.triangle_area(3, 5), 7.5)

  def test_decimal_sides(self):
    _, _, main = run_main()
    self.assertAlmostEqual(main.rectangle_area(2.5, 4), 10)
    self.assertAlmostEqual(main.triangle_area(1.5, 2), 1.5)

  def test_prints_results(self):
    out, _, main = run_main()
    self.assertRegex(out, r'(?<![\d.])8(?![\d.])')
    self.assertIn(str(main.triangle_area(2, 4)), out)

  def test_no_input(self):
    _, mock_input, _ = run_main()
    mock_input.assert_not_called()


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
