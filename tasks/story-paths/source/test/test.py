import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main(option):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=option) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


class TestStoryPaths(unittest.TestCase):
  def test_asks_for_option(self):
    _, mock_input = run_main("1")
    mock_input.assert_called_once()

  def test_first_path(self):
    out, _ = run_main("1")
    self.assertIn("első", out.lower())

  def test_second_path(self):
    out, _ = run_main("2")
    self.assertIn("második", out.lower())

  def test_invalid_option(self):
    out, _ = run_main("3")
    self.assertIn("rossz", out.lower())

  def test_empty_option(self):
    out, _ = run_main("")
    self.assertIn("rossz", out.lower())

  def test_paths_differ(self):
    outputs = {run_main(option)[0] for option in ("1", "2", "x")}
    self.assertEqual(len(outputs), 3)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
