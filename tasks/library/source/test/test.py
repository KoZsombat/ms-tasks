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


def new_books():
  return {"Könyv": "", "Másik könyv": "Anna"}


class TestLibrary(unittest.TestCase):
  def test_prints_results_and_status(self):
    _, out = run_main()
    self.assertEqual(out.strip().splitlines(), [
      "True",
      "False",
      "True",
      "False",
      "Egri csillagok: szabad",
      "A Pál utcai fiúk: Bence kölcsönözte ki",
      "Légy jó mindhalálig: szabad",
    ])

  def test_borrow_free_book(self):
    module, _ = run_main()
    books = new_books()
    self.assertIs(module.borrow_book(books, "Könyv", "Bence"), True)
    self.assertEqual(books["Könyv"], "Bence")

  def test_borrow_taken_book(self):
    module, _ = run_main()
    books = new_books()
    self.assertIs(module.borrow_book(books, "Másik könyv", "Bence"), False)
    self.assertEqual(books["Másik könyv"], "Anna")

  def test_borrow_unknown_book(self):
    module, _ = run_main()
    books = new_books()
    self.assertIs(module.borrow_book(books, "Nincs ilyen", "Bence"), False)
    self.assertEqual(books, new_books())

  def test_return_borrowed_book(self):
    module, _ = run_main()
    books = new_books()
    self.assertIs(module.return_book(books, "Másik könyv"), True)
    self.assertEqual(books["Másik könyv"], "")

  def test_return_invalid_book(self):
    module, _ = run_main()
    books = new_books()
    self.assertIs(module.return_book(books, "Könyv"), False)
    self.assertIs(module.return_book(books, "Nincs ilyen"), False)
    self.assertEqual(books, new_books())


if __name__ == '__main__':
  unittest.main()

# python3 -m unittest discover -s test -p "test.py" -v
