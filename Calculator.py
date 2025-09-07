num1 = float(input("Enter a number: "))
operator = input("Enter an operator (+ - * /) : ")
num2 = float(input("Enter a number : "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(round(num1 / num2,2))
else:
    print(f"{operator} is not a valid operator")
