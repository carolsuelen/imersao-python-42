#!/usr/bin/env python3


def array_of_names(persons):
    names = [f"{nome.capitalize()} {sobrenome.capitalize()}" for nome, sobrenome in persons.items()]
    return names


persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}


print(array_of_names(persons))

