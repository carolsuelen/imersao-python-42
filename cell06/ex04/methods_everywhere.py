#!/usr/bin/env python3

# chmod +x parameter_matching.py.

import sys


def shrink(str):
    slice_obj = slice(8)  # Cria um slice para os primeiros 8 caracteres
    print(str[slice_obj])

def enlarge(str):
    slice_obj = slice(8) 
     
    while len(str) < 8:
        str += 'Z'
    print(str[slice_obj])


def main():

    if len(sys.argv) == 1:
        print("nome")  # Se não houver argumentos, exibe "nome"
    else:
        # Itera sobre todos os argumentos passados ao programa
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                shrink(arg)  # Chama Shrink se a string tiver mais de 8 caracteres
            elif len(arg) < 8:
                enlarge(arg)  # Chama Enlarge se a string tiver menos de 8 caracteres
            else:
                print(arg)  # Exibe diretamente se a string tiver exatamente 8 caracteres

if __name__ == "__main__":
    main()

