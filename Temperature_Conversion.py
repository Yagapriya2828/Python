
unit = input ("Temperature in Celcius or Fahrenheit(C/F): ")
temp = float(input("Enter temperature : "))

if unit == "C" :
    temp = round((temp*9)/5 + 32,1)
    print(f"Temperature in Fahrenheit is: {temp}°F")
elif unit == "F" :
    temp = round((temp-32)*5/9,1)
    print(f"Temperature in Celcius is: {temp}°C")
else:
    print(f"{unit} is not a  valid unit")