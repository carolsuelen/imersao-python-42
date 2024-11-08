#!/usr/bin/env python3

# chmod +x calculator.py.

number1 = int(input("Give me the first number: "))

number2 = int(input("Give me the second number: "))

soma = number1 + number2
mult = number1 * number2
subt = number1 - number2
div = int(number1 / number2)

print("Thank you!")

print(str(number1) + " + " + str(number2) + " = " + str(soma))
print(str(number1) + " - " + str(number2) + " = " + str(subt))
print(str(number1) + " / " + str(number2) + " = " + str(div))
print(str(number1) + " * " + str(number2) + " = " + str(mult))
