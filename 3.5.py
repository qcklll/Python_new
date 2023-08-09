from random import*
seed(2019)
n = 5 #количество строк
m = 3 #количество столбцов

nested_list = [[randint(1,100) for _ in range(n)] for _ in range(m)]
print(nested_list)

row_move = int(input("Введите номер строки для удалени: ")) #переменная для движения по строкам
del(nested_list[row_move])
print(nested_list)
col_move = int(input("Введите номер столбца: "))#переменная для движения по столбцам
#для удаления столбца
for row in nested_list:
    del(row[col_move])

print(nested_list)




