#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        print(f"{param} {len(param)}")
