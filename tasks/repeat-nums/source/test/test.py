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


class TestRepeatNums(unittest.TestCase):
  def test_asks_for_answer(self):
    _, mock_input = run_main("1 2 3")
    mock_input.assert_called_once()

  def test_shows_numbers(self):
    out, _ = run_main("1 2 3")
    for number in ("1", "2", "3"):
      self.assertIn(number, out)

  def test_correct_answer(self):
    out, _ = run_main("1 2 3")
    self.assertIn("Ügyes", out)
    self.assertNotIn("Nem egyezik", out)

  def test_wrong_answer(self):
    out, _ = run_main("4 5 6")
    self.assertIn("Nem egyezik", out)
    self.assertNotIn("Ügyes", out)

  def test_wrong_order(self):
    out, _ = run_main("3 2 1")
    self.assertIn("Nem egyezik", out)
    self.assertNotIn("Ügyes", out)

  def test_empty_answer(self):
    out, _ = run_main("")
    self.assertIn("Nem egyezik", out)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
