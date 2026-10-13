age = int(input("Hány éves vagy? "))

if age < 18:
  print("Kiskorú vagy")
elif age < 65:
  print("Felnőtt vagy")
else:
  print("Nyugdíjas vagy")
