'''
a = (input("Введите целое число: "))
print(tuple(a))
reversed_a = a[::-1]
print(tuple(reversed_a))
'''
a = (input("Введите целое число: "))
if not a.isdigit():
    print("Ошибка: Введите целое число")
    exit()

digits = [int(digit) for digit in str(a)]
print(tuple(digits))

reversed_digits = digits[::-1]
print(tuple(reversed_digits))
