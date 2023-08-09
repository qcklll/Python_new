text = input("Введите текст: ")
dictionary = {}

for char in text:
    if char not in dictionary.keys():
        value = text.replace(char, "", 1)
        dictionary[char] = value

print(dictionary)
