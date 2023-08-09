txt_first = input("Введите первый текст: ")
txt_second = input("Введите второй текст: ")
len_txt = max(len(txt_first), len(txt_second))
new_txt = ""
a = 0

while a < len_txt:
    if a < len(txt_first):
        new_txt += txt_first[a]
    else:
        new_txt += "*"
    if a < len(txt_second):
        new_txt += txt_second[a]
    else:
        new_txt += "*"
    a += 1

print(new_txt)

    

    
