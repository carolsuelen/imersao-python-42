#!/usr/bin/env python3

# chmod +x multiplication_table.py.

number = int(input("Enter a number: " + "\n"))

for count in range(10):
# print("%d x %d = %d" % (count, number, number*count))
    print(f"{count} x {number} = {number*count} ")
