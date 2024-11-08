#!/usr/bin/env python3

# Método que recebe um parâmetro e adiciona 1 a ele
def add_one(n):
    n += 1
    return n

if __name__ == "__main__":
    # Inicializando a variável no corpo do programa
    my_var = 10
    print(f"Valor inicial de my_var: {my_var}")

    # Chamando o método add_one e passando my_var
    my_var = add_one(my_var)
    print(f"Valor de my_var após chamar add_one: {my_var}")

    # Exibindo o valor da variável novamente
    print(f"Valor final de my_var no corpo principal: {my_var}")

