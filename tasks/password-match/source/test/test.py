import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main(answer):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=answer) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


class TestPasswordMatch(unittest.TestCase):
  def test_asks_for_password(self):
    _, mock_input = run_main("password")
    mock_input.assert_called_once()

  def test_correct_password(self):
    out, _ = run_main("password")
    self.assertIn("Helyes", out)
    self.assertNotIn("Nem egyezik", out)

  def test_wrong_password(self):
    out, _ = run_main("123456")
    self.assertIn("Nem egyezik", out)
    self.assertNotIn("Helyes", out)

  def test_case_sensitive(self):
    out, _ = run_main("Password")
    self.assertIn("Nem egyezik", out)
    self.assertNotIn("Helyes", out)

  def test_empty_password(self):
    out, _ = run_main("")
    self.assertIn("Nem egyezik", out)

  def test_accented_password(self):
    out, _ = run_main("Árvíztűrő")
    self.assertIn("Nem egyezik", out)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
