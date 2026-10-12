nums = ["1", "2", "3"]

print("repeat this:", *nums)

input = input("Válaszod: ")

input_list = input.split(" ")

if (nums == input_list):
  print("Ügyes vagy")
else:
  print(f"Nem egyezik meg")
