#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("none")
    sys.exit()
else:
    word = input(("What was the parameter? " ))
    if word != sys.argv[1]:
        print("Nope, sorry...")
    else:
        print("Good job!")
    