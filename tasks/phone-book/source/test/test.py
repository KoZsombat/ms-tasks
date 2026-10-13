import contextlib
import importlib
import io
import sys
import unittest
from unittest.mock import patch


def run_main(name):
  sys.modules.pop('main', None)
  out = io.StringIO()
  with patch('builtins.input', return_value=name) as mock_input, contextlib.redirect_stdout(out):
    module = importlib.import_module('main')
  return module, out.getvalue().strip(), mock_input


class TestPhoneBook(unittest.TestCase):
  def test_asks_for_name(self):
    _, _, mock_input = run_main("Anna")
    mock_input.assert_called_once()

  def test_finds_contact(self):
    _, out, _ = run_main("Anna")
    self.assertEqual(out, "Anna telefonszáma: +36301234567")

  def test_finds_other_contact(self):
    _, out, _ = run_main("Bence")
    self.assertEqual(out, "Bence telefonszáma: +36207654321")

  def test_finds_accented_contact(self):
    _, out, _ = run_main("Árpád")
    self.assertEqual(out, "Árpád telefonszáma: +36701112233")

  def test_unknown_contact(self):
    for name in ("Béla", "", "anna"):
      _, out, _ = run_main(name)
      self.assertEqual(out, "Nincs ilyen névjegy", f"name {name!r}")

  def test_find_contact_function(self):
    module, _, _ = run_main("Anna")
    book = {"Kata": "123", "Dani": "456"}
    self.assertEqual(module.find_contact(book, "Dani"), "456")
    self.assertIsNone(module.find_contact(book, "Éva"))


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
