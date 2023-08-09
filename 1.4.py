# Ввод размера списка
n = int(input("Введите размер списка: "))

# Создание списка со степенями двойки
powers_of_two = [2 ** i for i in range(n)]

# Вывод списка
print("Список степеней двойки:")
for number in powers_of_two:
    print(number)
