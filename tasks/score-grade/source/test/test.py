import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main(value):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=value) as mock_input, contextlib.redirect_stdout(out):
    importlib.import_module('main')
  return out.getvalue().strip(), mock_input


class TestScoreGrade(unittest.TestCase):
  def check_grades(self, grade, scores):
    for score in scores:
      out, _ = run_main(score)
      self.assertEqual(out, grade, f"score {score}")

  def test_asks_for_score(self):
    _, mock_input = run_main("50")
    mock_input.assert_called_once()

  def test_grade_1(self):
    self.check_grades("1", ["0", "20", "39"])

  def test_grade_2(self):
    self.check_grades("2", ["40", "50", "59"])

  def test_grade_3(self):
    self.check_grades("3", ["60", "70", "79"])

  def test_grade_4(self):
    self.check_grades("4", ["80", "85", "89"])

  def test_grade_5(self):
    self.check_grades("5", ["90", "95", "100"])


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
