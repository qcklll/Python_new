a = int(input("Введите длины сторон треугольника"))
b = int(input())
c = int(input())
print(a, b, c)

res = "может" if a+b > c and a+c > b and b+c > a else "не может"

print("Треугольник "+res+" существовать")
