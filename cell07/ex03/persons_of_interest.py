#!/usr/bin/env python3


def famous_births(women_scientists):
    sorted_persons = sorted(women_scientists.items(), key=lambda x: x[1]['date_of_birth'])

    # A função sorted() em Python é usada para ordenar qualquer tipo de iterável (como listas, tuplas, dicionários, etc.)
    #  de forma ascendente ou personalizada. Ela retorna uma nova lista ordenada e não modifica o iterável original.

    # A função sorted() retorna uma nova lista contendo os elementos ordenados.
    # Importante: O iterável original não é modificado. O sorted() cria uma cópia ordenada do iterável e a retorna.
    

    # Display the sorted persons in the specified format
    for _, details in sorted_persons:
        name = details['name']
        birth_date = details['date_of_birth']
        birth_year = birth_date.split('-')[0]  # Extracting only the year part of the birth date
        print(f"{name} is a great scientist born in {birth_year}.")


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}


famous_births(women_scientists)

