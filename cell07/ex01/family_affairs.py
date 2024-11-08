#!/usr/bin/env python3


def find_the_redheads(dupont_family):
    red_hair = [nome for nome, cor in dupont_family.items() if cor == "red"]
    return red_hair


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}


print(find_the_redheads(dupont_family))

