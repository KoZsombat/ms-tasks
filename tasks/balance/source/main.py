income = int(input("Mennyi kerestél? "))
expense = int(input("Mennyi költöttél? (0 ha nincs több) "))
expenses = 0

while(expense != 0):
  expenses += expense
  expense = int(input("Mennyi költöttél? (0 ha nincs több) "))

print(f"Ennyi pénzed mardt: {income-expenses}")
