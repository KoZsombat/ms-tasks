import contextlib
import importlib
import io
import sys
import unittest


def run_main():
  sys.modules.pop('main', None)
  out = io.StringIO()
  with contextlib.redirect_stdout(out):
    module = importlib.import_module('main')
  return module, out.getvalue()


class TestStudyTime(unittest.TestCase):
  def test_prints_totals(self):
    _, out = run_main()
    self.assertEqual(out.strip().splitlines(), [
      "Matek: 90 perc",
      "Történelem: 65 perc",
      "Angol: 50 perc",
    ])

  def test_sums_same_subject(self):
    module, _ = run_main()
    result = module.total_time([["Fizika", 20], ["Fizika", 40], ["Fizika", 5]])
    self.assertEqual(result, {"Fizika": 65})

  def test_separate_subjects(self):
    module, _ = run_main()
    result = module.total_time([["Matek", 30], ["Angol", 45], ["Matek", 15]])
    self.assertEqual(result, {"Matek": 45, "Angol": 45})

  def test_single_session(self):
    module, _ = run_main()
    result = module.total_time([["Biológia", 25]])
    self.assertEqual(result, {"Biológia": 25})

  def test_empty_sessions(self):
    module, _ = run_main()
    self.assertEqual(module.total_time([]), {})

  def test_accented_subject_and_zero_minutes(self):
    module, _ = run_main()
    result = module.total_time([["Földrajz", 0], ["Földrajz", 10], ["Ének", 0]])
    self.assertEqual(result, {"Földrajz": 10, "Ének": 0})


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
