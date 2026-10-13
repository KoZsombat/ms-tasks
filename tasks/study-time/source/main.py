sessions = [
  ["Matek", 60],
  ["Történelem", 45],
  ["Matek", 30],
  ["Angol", 50],
  ["Történelem", 20]
]

def total_time(sessions):
  totals = {}

  for session in sessions:
    subject = session[0]
    minutes = session[1]

    if subject in totals:
      totals[subject] += minutes
    else:
      totals[subject] = minutes

  return totals

totals = total_time(sessions)

for subject in totals:
  print(f"{subject}: {totals[subject]} perc")
