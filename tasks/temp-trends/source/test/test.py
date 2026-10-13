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


class TestTempTrends(unittest.TestCase):
  def test_prints_trend_counts(self):
    _, out = run_main()
    self.assertEqual(out.strip().splitlines(), [
      "Emelkedő napok: 4",
      "Csökkenő napok: 3",
      "Változatlan napok: 2",
    ])

  def test_rising_temperatures(self):
    module, _ = run_main()
    self.assertEqual(tuple(module.trends([1, 2, 3, 4])), (3, 0, 0))

  def test_falling_temperatures(self):
    module, _ = run_main()
    self.assertEqual(tuple(module.trends([4, 3, 2, 1])), (0, 3, 0))

  def test_constant_temperatures(self):
    module, _ = run_main()
    self.assertEqual(tuple(module.trends([5, 5, 5])), (0, 0, 2))

  def test_mixed_temperatures(self):
    module, _ = run_main()
    result = module.trends([12, 14, 15, 15, 13, 11, 11, 16, 18, 17])
    self.assertEqual(tuple(result), (4, 3, 2))

  def test_short_lists(self):
    module, _ = run_main()
    self.assertEqual(tuple(module.trends([])), (0, 0, 0))
    self.assertEqual(tuple(module.trends([7])), (0, 0, 0))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
