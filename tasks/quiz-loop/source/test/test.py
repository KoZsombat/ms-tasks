import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main(answers):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', side_effect=answers) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue(), mock_input


class TestQuizLoop(unittest.TestCase):
  def test_correct_first_answer_asks_once(self):
    _, mock_input = run_main(["56"])
    self.assertEqual(mock_input.call_count, 1)

  def test_correct_answer_prints_message(self):
    out, _ = run_main(["56"])
    self.assertTrue(out.strip() != "")

  def test_asks_again_after_wrong_answer(self):
    _, mock_input = run_main(["10", "56"])
    self.assertEqual(mock_input.call_count, 2)

  def test_asks_until_correct_answer(self):
    _, mock_input = run_main(["1", "2", "3", "4", "56"])
    self.assertEqual(mock_input.call_count, 5)

  def test_stops_after_correct_answer(self):
    _, mock_input = run_main(["1", "56", "2", "3"])
    self.assertEqual(mock_input.call_count, 2)

  def test_empty_and_accented_answers_are_wrong(self):
    _, mock_input = run_main(["", "Árvíztűrő", "56"])
    self.assertEqual(mock_input.call_count, 3)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
