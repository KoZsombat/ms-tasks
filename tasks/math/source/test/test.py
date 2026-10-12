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


class TestMath(unittest.TestCase):
  def test_add(self):
    module, _ = run_main()
    self.assertEqual(module.add(2, 3), 5)
    self.assertEqual(module.add(-1, 1), 0)

  def test_subtract(self):
    module, _ = run_main()
    self.assertEqual(module.subtract(5, 3), 2)
    self.assertEqual(module.subtract(1, 2), -1)

  def test_multiply(self):
    module, _ = run_main()
    self.assertEqual(module.multiply(4, 3), 12)
    self.assertEqual(module.multiply(5, 0), 0)

  def test_divide_numbers(self):
    module, _ = run_main()
    self.assertEqual(module.divide(6, 3), 2)
    self.assertEqual(module.divide(1, 2), 0.5)

  def test_divide_by_zero(self):
    module, _ = run_main()
    self.assertEqual(module.divide(5, 0), 0)

  def test_prints_results(self):
    _, out = run_main()
    lines = out.strip().splitlines()
    self.assertEqual(len(lines), 4)
    for value in ("3", "-1", "2", "0.5"):
      self.assertTrue(any(value in line for line in lines), value)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
