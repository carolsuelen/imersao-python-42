#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys


def downcase_it():

    if len(sys.argv) == 1:
        print("none")
        sys.exit()
    else:
        for arg in sys.argv[1:]:
            print(arg.lower())

    return



downcase_it()   