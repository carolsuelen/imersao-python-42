#!/usr/bin/env python3


def average(class_scores):
    soma_pontuacoes = sum(class_scores.values())

    # Calcular o número de alunos
    numero_alunos = len(class_scores)

    # Calcular a média
    media_turma = soma_pontuacoes / numero_alunos

    # Retornar a média
    return media_turma


class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}


print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
