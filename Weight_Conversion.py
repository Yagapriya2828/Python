
weight = float(input("Enter your weight: "))
unit = input("Kilograms(K) or Pounds(L): ")

if unit == "K":
    weight = round(weight * 2.205)
    unit = "Lbs"
elif unit == "L":
    weight = round(weight * 0.45)
    unit = "Kgs"
else:
    print("Enter a valid unit")

print(f"Your weight is: {weight} {unit}")
