contacts = {
  "Anna": "+36301234567",
  "Bence": "+36207654321",
  "Árpád": "+36701112233"
}

def find_contact(contacts, name):
  if name in contacts:
    return contacts[name]

  return None

name = input("Kit keresel? ")
number = find_contact(contacts, name)

if number is None:
  print("Nincs ilyen névjegy")
else:
  print(f"{name} telefonszáma: {number}")
