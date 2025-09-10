
weight = float(input("Enter your weight: "))
unit = input("Kilograms(K) or Pounds(L): ")

if unit == "K":
    weight = round(weight * 2.205)
    unit = "Lbs"
    print(f"Your weight is: {weight} {unit}")
elif unit == "L":
    weight = round(weight * 0.45)
    unit = "Kgs"
    print(f"Your weight is: {weight} {unit}")
else:
    print("Enter a valid unit")


