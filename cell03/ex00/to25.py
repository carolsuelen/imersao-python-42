#!/usr/bin/env python3

# chmod +x to25.py.

number = int(input("Enter a number less than 25 " + "\n"))

if number > 25:
    print("Error")
else:
    while number <= 25:
        print("Inside the loop, my variable is " + str(number))
        number += 1