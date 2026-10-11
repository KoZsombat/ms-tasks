import math

scores = [20, 40, 60, 80, 85]

def passed(v):
  return v >= 40

print(f"Átlag: {sum(scores) / len(scores)}, legmagasabb: {max(scores)}, átment {len(list(filter(passed, scores)))} tanuló")
