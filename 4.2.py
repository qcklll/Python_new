a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

a_str = str(a)
b_str = str(b)

A = set(a_str)
B = set(b_str)

common_digits = A.intersection(B)

print("Цифры, которые есть в обоих числах:")
for digit in common_digits:
    print(digit, end=" ")

