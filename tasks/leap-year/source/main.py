year = int(input("Milyen évet írunk? "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
  print("Szökő év")
else:
  print("Nincs szökő év")
