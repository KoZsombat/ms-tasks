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


class TestAgeMessage(unittest.TestCase):
  def test_asks_for_age(self):
    _, mock_input = run_main("30")
    mock_input.assert_called_once()

  def test_minor_message(self):
    for age in ("0", "10", "17"):
      out, _ = run_main(age)
      self.assertEqual(out, "Kiskorú vagy", age)

  def test_adult_message(self):
    for age in ("30", "50"):
      out, _ = run_main(age)
      self.assertEqual(out, "Felnőtt vagy", age)

  def test_retired_message(self):
    for age in ("70", "100"):
      out, _ = run_main(age)
      self.assertEqual(out, "Nyugdíjas vagy", age)

  def test_age_18_is_adult(self):
    out, _ = run_main("18")
    self.assertEqual(out, "Felnőtt vagy")

  def test_age_65_is_retired(self):
    out, _ = run_main("65")
    self.assertEqual(out, "Nyugdíjas vagy")


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
