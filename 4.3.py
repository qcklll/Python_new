text = input("Введите ваш текст: ")
text_list = []
for i in text:
    text_list.append(i)
A = set("аоуэыяёеюи")
A.intersection_update(text_list)
print("В вашем тексте есть такие гласные буквы как:", "".join(A))

