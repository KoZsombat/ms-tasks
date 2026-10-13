temps = [
  12, 14, 15, 15, 13, 11, 11, 16, 18, 17
]

def trends(temps):
  rising = 0
  falling = 0
  same = 0

  for i in range(1, len(temps)):
    if temps[i] > temps[i - 1]:
      rising += 1
    elif temps[i] < temps[i - 1]:
      falling += 1
    else:
      same += 1

  return rising, falling, same

rising, falling, same = trends(temps)

print(f"Emelkedő napok: {rising}")
print(f"Csökkenő napok: {falling}")
print(f"Változatlan napok: {same}")
