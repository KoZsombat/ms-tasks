import contextlib
import importlib
import io
import re
import sys
import unittest
from unittest.mock import patch


def run_main():
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value='') as mock_input, contextlib.redirect_stdout(out):
    module = importlib.import_module('main')
  return out.getvalue(), mock_input, module


class TestScores(unittest.TestCase):
  def test_prints_average(self):
    out, _, _ = run_main()
    self.assertRegex(out, r'\b57(\.0+)?\b')

  def test_prints_highest(self):
    out, _, _ = run_main()
    self.assertRegex(out, r'\b85\b')

  def test_prints_passed_count(self):
    out, _, _ = run_main()
    self.assertRegex(out, r'(?<![\d.])4(?![\d.])')

  def test_passed_at_threshold(self):
    _, _, module = run_main()
    self.assertTrue(module.passed(40))
    self.assertTrue(module.passed(85))

  def test_failed_below_threshold(self):
    _, _, module = run_main()
    self.assertFalse(module.passed(39))
    self.assertFalse(module.passed(0))

  def test_no_input(self):
    _, mock_input, _ = run_main()
    mock_input.assert_not_called()


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
