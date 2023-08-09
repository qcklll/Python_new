number = input("Введите целое число: ")

counters = [0] * 10  # Создаем список счетчиков для каждой цифры от 0 до 9

for digit in number:
    if digit.isdigit():
        counters[int(digit)] += 1

for i in range(10):
    print("Количество цифр", i, "в вашем числе:", counters[i])
