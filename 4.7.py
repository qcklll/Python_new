text = input("Введите ваш текст: ")
num_text = []
letter_count = {}

for i in text:
    num_text.append(i)

for letter in num_text:
    letter_count[letter] = num_text.count(letter)

print(letter_count)

""" Версия чат гпт с применением метода
from collections import Counter

text = input("Введите ваш текст: ")
letter_count = dict(Counter(text))

print(letter_count)
"""
