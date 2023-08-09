"""
numb = [12,3,456,78]
result = ""
for chisla in numb:
    result +=str(chisla)

print ("Результат:", result)
"""
num_list = []

# Ввод чисел с клавиатуры
while True:
    num = input("Введите число (или 'q' для выхода): ")
    if num == 'q':
        break
    else:
        num_list.append(num)

# Переменная для хранения объединенного числа
result = "".join(num_list)

print("Результат:", result)
