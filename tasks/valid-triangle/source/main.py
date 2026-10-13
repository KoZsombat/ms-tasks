a = int(input("Háromszög egyik oldala: "))
b = int(input("Háromszög másik oldala: "))
c = int(input("Háromszög harmadik oldala: "))

if (a > 0 and b > 0 and c > 0 and (a + b) > c and (a + c) > b and (c + b) > a):
  print("Valódi háromszög")
else:
  print("Nem valódi háromszög")
