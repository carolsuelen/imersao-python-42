#!/usr/bin/env python3

# chmod +x multi.py.

number1 = int(input("Enter the first number: "))

number2 = int(input("Enter the second number: "))
total = number1*number2

print(str(number1) + " x " + str(number2) + " = " + str(total))

if total > 0:
    print("The result is positive")
elif total < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")
