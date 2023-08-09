first_dict = {
    "L": "lol",
    "D": "diablo",
    "K": "king",
    "J": "jewish",
    "Z": "zorro",
    "P": "pizza"
}

second_dict = {
    "Q": "qwerty",
    "S": "set",
    "V": "victory",
    "P": "pizza",
    "L": "lol",
    "N": "nuts"
}

combined_dict = {}

for key in first_dict.keys():
    if key in second_dict.keys():
        combined_dict[key] = {first_dict[key], second_dict[key]}

print(combined_dict)

