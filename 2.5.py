spisok = []
number_list = []
number_list_out = []

max_numbers = int(input("Введите границу числа: "))

while True:
    num = input("Введите число (или 'q' для выхода:) ")
    if num == 'q':
        break
    else:
        spisok.append(int(num))
for k in range (1, max_numbers + 1):
    number_list.append(k)

for i in range(len(number_list)):
    if number_list[i] not in spisok:
        number_list_out.append(number_list[i])
        
print("Список чисел:", spisok)
print("Список натуральных чисел:", number_list)
print("Сумма чисел без учета списка:", sum(number_list_out))

