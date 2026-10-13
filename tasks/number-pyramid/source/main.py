rows = int(input("Hány sort írjak ki? "))

for i in range(1, rows + 1):
  line = ""
  for j in range(1, i + 1):
    line = line + str(j) + " "
  print(line.strip())
