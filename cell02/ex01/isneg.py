#!/usr/bin/env python3

# chmod +x isneg.py.


# • Create a program called password.py.
# • This program should be executable.
# • The program should have a variable containing a password.
# password = "Python is awesome"
# • When executed, the program should prompt for a password to be entered.
# • If the password is correct, the program should display "ACCESS GRANTED";
# otherwise, it should display "ACCESS DENIED."

number = int(input())

if number < 0:
 print("This number is negative.")
elif number > 0:
 print("This number is positive")
elif number == 0:
 print("This number is both positive and negative.")