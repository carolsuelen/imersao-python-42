#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys

if len(sys.argv) == 1:
        print("none")  # Se não houver parâmetros, exibe "nenhum"
else:
    # Para cada argumento passado ao script (começando do índice 1)
    for arg in sys.argv[1:]:
        match arg:
            case _ if arg.endswith("ism"):
                continue  # Ignora o argumento se terminar com "ism"
            case _:
                print(arg + "ism")