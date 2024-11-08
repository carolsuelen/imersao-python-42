#!/usr/bin/env python3

# chmod +x advanced_multi.py.
import sys

# print(sys.argv)

if len(sys.argv) > 1:
    print("none")
    sys.exit()

i = 0

while i < 11:
    j = 0
    aux = (f"Table de {i}: ")
    while j < 11:
        x = i * j
        aux += (f"{x} ")
        j += 1
    i += 1
    print(aux)    