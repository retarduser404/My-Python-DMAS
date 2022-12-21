# My Calculator!

first: = input("Enter First Number : ")
second: = input("Enter Second Number : ")
operator = input("Enter Operator (+, -, /, %) : ")
first = int(first)
second = int(second)
if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operation")
