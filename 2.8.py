"""
a = input("Введите целое число от 1 до 7: ")
if int(a) == 1:
    print("Понедельник")
elif int(a) == 2:
    print("Вторник")
elif int(a) == 3:
    print("Среда")
elif int(a) == 4:
    print("Четверг")
elif int(a) == 5:
    print("Пятница")
elif int(a) == 6:
    print("Суббота")
elif int(a) == 7:
    print("Воскресенье")

else:
    print("Вы ввели неккоретные данные")
"""
day_names = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье"
]
try:
    a = input("Введите целое число от 1 до 7: ")
    a = int(a)

    if 1 <= a <= 7:
        print(day_names[a-1])
    else:
        print("Вы ввели неверные данные")
except:
    print("Вы ввели неверные данные")
