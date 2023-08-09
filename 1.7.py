n = int(input("Введите число для вычисления факториала: "))

if n < 0:
    print("Ошибка: Введите положительное число!")
else:
    faktorial = 1
    for k in range(1, n+1):
        faktorial *= k

    print("Факториал числа", n, "равен:", faktorial)
