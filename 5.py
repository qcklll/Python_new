txt = input("Введите ваш текст")
new_txt = txt
a = ""

for k in new_txt:
    a = new_txt[k]
    new_txt[k] += new_txt[k+1]

print(new_txt)
