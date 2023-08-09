num = 10

L=lambda n: 2*n+1

print("Нечётные числа:")

for k in range(num):
    print(L(k), end=" ")

L = lambda n: 2**n

print("\nСтепени двойки:")
for k in range(num):
    print(L(k), end=" ")

#Прямой вызов лямбда функции
print("\nКвадраты чисел:")
for k in range(num):
    print((lambda x: x*x)(k+1), end=" ")

#Обычная функция:
def calc(x, y):
    return x+y

#Использование функции в лямбда-выражении
F = lambda x, y: calc(x, y)
# Переменной присваивается имя функции
f = calc
# Имени функции присвается лямба-выражение
calc = lambda x, y: x*y

print("\nВызов F(3,5):", F(3,5))
print("Вызов f(3,5):", f(3,5))
print("Вызов calc(3,5):", calc(3,5))
