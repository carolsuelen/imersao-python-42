#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys

def main():
    # Verifica se o número de parâmetros é 1
    if len(sys.argv) != 2:
        print("none")
        return
    
    # Pega a string do argumento passado
    input_string = sys.argv[1]
    
    # Verifica se há o caractere 'z' na string
    found_z = False
    for char in input_string:
        if char == 'z':
            print("z")
            found_z = True
    
    # Se não encontrou nenhum 'z', imprime "none" uma única vez
    if not found_z:
        print("none")

if __name__ == "__main__":
    main()