import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main(name):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=name) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


class TestGreeting(unittest.TestCase):
  def test_greets_by_name(self):
    out, _ = run_main("Zsombor")
    self.assertIn("Zsombor", out)

  def test_asks_for_name(self):
    _, mock_input = run_main("Zsombor")
    mock_input.assert_called_once()

  def test_accented_name(self):
    out, _ = run_main("Árvíztűrő")
    self.assertIn("Árvíztűrő", out)

  def test_empty_name(self):
    out, _ = run_main("")
    self.assertTrue(out.endswith("\n"))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
