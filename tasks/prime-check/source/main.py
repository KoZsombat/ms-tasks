num = int(input("Írj be egy egész számot: "))

is_prime = num > 1

for i in range(2, num):
  if num % i == 0:
    is_prime = False

if is_prime:
  print("Prímszám")
else:
  print("Nem prímszám")
