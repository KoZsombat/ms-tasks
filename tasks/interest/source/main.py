principal = int(input("Mennyi a tőke? "))
rate = int(input("Mennyi az éves kamatláb (%)? "))
time = int(input("Hány évre? "))

print(f"Kamat: {principal * rate * time / 100}")
