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
  return out.getvalue(), module


class TestLargerNumber(unittest.TestCase):
  def test_first_is_larger(self):
    _, main = run_main()
    self.assertEqual(main.Nagyobb(5, 2), 5)

  def test_second_is_larger(self):
    _, main = run_main()
    self.assertEqual(main.Nagyobb(2, 7), 7)

  def test_equal_numbers(self):
    _, main = run_main()
    self.assertEqual(main.Nagyobb(4, 4), 4)

  def test_negative_numbers(self):
    _, main = run_main()
    self.assertEqual(main.Nagyobb(-3, -8), -3)
    self.assertEqual(main.Nagyobb(-10, 0), 0)

  def test_float_numbers(self):
    _, main = run_main()
    self.assertEqual(main.Nagyobb(2.5, 2.7), 2.7)

  def test_prints_example_result(self):
    out, _ = run_main()
    self.assertIn("3", out)


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
