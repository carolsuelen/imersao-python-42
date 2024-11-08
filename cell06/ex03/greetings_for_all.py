#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys


def greetings(nome="nobre estranho"):
    # Verifica se o parâmetro é uma string
    if not isinstance(nome, str):
        print("Error! It was not a name.$")
    else:
        print(f"Hello, {nome}!")



greetings("Alexandra")   
greetings("Will")
greetings()
greetings(42)
