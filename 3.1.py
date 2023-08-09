a = input("Введите текст: ")
n = int(input("Введите шаг для кортежа: "))
print(tuple(a))
B = a[::n]
print(tuple(B))

