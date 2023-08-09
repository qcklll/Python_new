txt = input("Введите текст: ")
txt = txt.lower()

words = txt.split(" ")
revers_words = words[::-1]
print(" ".join(revers_words))



