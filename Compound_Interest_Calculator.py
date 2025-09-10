
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter principle amount: "))
    if principle < 0:
        print("principle cannot be less than zero, please enter again")
    else:
        break

while True:
    rate = float(input("Enter interest rate: "))
    if rate < 0:
        print("Interest rate cannot be less than zero, please enter again")
    else:
        break

while True:
    time = int(input("Enter number of years: "))
    if time < 0:
        print("time cannot be less than zero, please enter again")
    else:
        break

compound_interest = principle * pow(1 + rate/100,time)
print(f"Balance after time {time} is ${compound_interest:.2f}")
