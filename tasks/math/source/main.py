def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if (b != 0):
    return a / b
  else:
    return 0

print(f"Add {add(1,2)}")
print(f"Subtract {subtract(1,2)}")
print(f"Multiply {multiply(1,2)}")
print(f"Divide {divide(1,2)}")
