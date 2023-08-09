txt = input("Введите ваш текст: ")
new_txt = ""
a = 0

while a < len(txt) - 2:
        new_txt += txt[a+2] + txt[a+1]+ txt[a]
        a += 2




print("Результат: ", new_txt)


