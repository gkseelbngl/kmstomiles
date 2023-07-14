print("How many kilometers did you drive today?")
kms = input()
miles = float(kms) * 0.621371192
romiles = round(miles, 2)
print(f"Your {kms} km ride is was {romiles} mil")
# round(thing to round, how many decimal points)
