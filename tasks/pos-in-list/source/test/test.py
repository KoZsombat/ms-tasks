import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main():
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input') as mock_input, contextlib.redirect_stdout(out):
    module = importlib.import_module('main')
  return module, out.getvalue(), mock_input


class TestPosInList(unittest.TestCase):
  def test_list_contents(self):
    module, _, _ = run_main()
    self.assertEqual(module.list, [1, 2, 3, 4, 5])

  def test_prints_one_line(self):
    _, out, _ = run_main()
    self.assertEqual(len(out.strip().splitlines()), 1)

  def test_prints_position_of_three(self):
    _, out, _ = run_main()
    self.assertEqual(out.strip(), "2")

  def test_output_matches_list_index(self):
    module, out, _ = run_main()
    self.assertEqual(int(out.strip()), module.list.index(3))

  def test_does_not_ask_for_input(self):
    _, _, mock_input = run_main()
    mock_input.assert_not_called()


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
