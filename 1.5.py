ost = [5*k+3 for k in range(1,11)]
print(ost)
print(list(reversed(ost)))
"""
Я бы решил поставленную задачу с использованием цикла for и условного оператора if, чтобы создать список чисел, удовлетворяющих условию.

Вот пример программы, которая решает задачу:

python
Copy code
# Создание списка чисел, удовлетворяющих условию
ost = []
for k in range(1, 11):
    num = 5 * k + 3
    ost.append(num)

# Вывод списка в прямом порядке
print("Список в прямом порядке:")
print(ost)

# Вывод списка в обратном порядке
print("Список в обратном порядке:")
reversed_ost = list(reversed(ost))
print(reversed_ost)
В этом примере мы используем цикл for для создания списка ost. В каждой итерации цикла мы вычисляем число, удовлетворяющее условию 5*k + 3,
где k принимает значения от 1 до 10. Мы добавляем это число в список ost с помощью метода append().

Затем мы выводим список ost в прямом порядке с помощью функции print.
Для вывода списка в обратном порядке мы используем функцию reversed вместе с функцией list, чтобы создать обратный список reversed_ost, и выводим его.
Этот код решает задачу, создавая список чисел, удовлетворяющих условию, и выводит его как в прямом, так и в обратном порядке.
Оба подхода (ваш и мой) корректно решают поставленную задачу. Выбор конкретного подхода может зависеть от предпочтений программиста и требований конкретной задачи.

"""
