num = int(input("Írj be egy pozitív egész számot: "))

result = 1
for i in range(1, num + 1):
  result = result * i

print(f"{num}! = {result}")
