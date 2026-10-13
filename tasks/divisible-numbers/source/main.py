divisor = int(input("Melyik számmal osztható számokat írjam ki? "))

for i in range(1, 101):
  if i % divisor == 0:
    print(i)
