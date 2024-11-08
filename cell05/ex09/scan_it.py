#!/usr/bin/env python3

import sys


# if len(sys.argv) != 3:
#     print("none")
# else:
#     palavra_chave = sys.argv[1]
#     texto = sys.argv[2]
    
#     ocorrencias = texto.count(palavra_chave)
    
#     if ocorrencias == 0:
#         print("none")
#     else:
#         print(ocorrencias)

# Usando a biblioteca re:

import re  # Importando a biblioteca re

# Verificando se o número de parâmetros é diferente de 2 (excluindo o nome do script)
if len(sys.argv) != 3:
    print("none")  # Se o número de parâmetros for diferente de 2, imprime "none"
else:
    palavra_chave = sys.argv[1]
    texto = sys.argv[2]
    
    # Verificando se a palavra-chave aparece no texto
    if palavra_chave not in texto:
        print("none")  # Se a palavra-chave não aparece no texto, imprime "none"
    else:
        # Usando re.findall() para encontrar todas as ocorrências da palavra-chave
        ocorrencias = len(re.findall(re.escape(palavra_chave), texto))  # re.escape é útil para tratar caracteres especiais
        print(ocorrencias)  # Imprime o número de ocorrências
