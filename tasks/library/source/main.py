books = {
  "Egri csillagok": "",
  "A Pál utcai fiúk": "",
  "Légy jó mindhalálig": ""
}

def borrow_book(books, title, name):
  if title not in books or books[title] != "":
    return False

  books[title] = name
  return True

def return_book(books, title):
  if title not in books or books[title] == "":
    return False

  books[title] = ""
  return True

print(borrow_book(books, "Egri csillagok", "Anna"))
print(borrow_book(books, "Egri csillagok", "Bence"))
print(return_book(books, "Egri csillagok"))
print(return_book(books, "Egri csillagok"))

borrow_book(books, "A Pál utcai fiúk", "Bence")

for title in books:
  if books[title] == "":
    print(f"{title}: szabad")
  else:
    print(f"{title}: {books[title]} kölcsönözte ki")
