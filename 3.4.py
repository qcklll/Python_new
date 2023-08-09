def fill_snake_list(n):
    nested_list = [[0 for _ in range(n)] for _ in range(n)]  # Создаем вложенный список из нулей
    num = 1  # Значение для заполнения списка
    row_start = 0  # Начальная позиция строки
    row_end = n - 1  # Конечная позиция строки
    col_start = 0  # Начальная позиция столбца
    col_end = n - 1  # Конечная позиция столбца

    while num <= n * n:
        # Заполнение верхней строки слева направо
        for i in range(col_start, col_end + 1):
            nested_list[row_start][i] = num
            num += 1
        row_start += 1

        # Заполнение правого столбца сверху вниз
        for i in range(row_start, row_end + 1):
            nested_list[i][col_end] = num
            num += 1
        col_end -= 1

        # Заполнение нижней строки справа налево
        for i in range(col_end, col_start - 1, -1):
            nested_list[row_end][i] = num
            num += 1
        row_end -= 1

        # Заполнение левого столбца снизу вверх
        for i in range(row_end, row_start - 1, -1):
            nested_list[i][col_start] = num
            num += 1
        col_start += 1

    return nested_list


n = int(input("Введите размер списка: "))
result = fill_snake_list(n)
for row in result:
    print(row)
