#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys


if len(sys.argv) != 3:
    print("none")
    sys.exit() 
else:
    start = int(sys.argv[1])
    stop = int(sys.argv[2])

    matrix = list(range(start, stop + 1))

    print(matrix)

