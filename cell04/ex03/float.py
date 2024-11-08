#!/usr/bin/env python3

# chmod +x float.py.


number = float(input("Give me a number: "))

if number % 1 != 0:
# if number.is_integer():
    print("This number is decimal")
else:
    print("This number is a integer")

