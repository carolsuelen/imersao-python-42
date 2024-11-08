#!/usr/bin/env python3

import sys


if len(sys.argv) != 3:
    print("none")
else:
    palavra_chave = sys.argv[1]
    texto = sys.argv[2]
    
    ocorrencias = texto.count(palavra_chave)
    
    if ocorrencias == 0:
        print("none")
    else:
        print(ocorrencias)
