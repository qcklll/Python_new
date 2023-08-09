import copy
try:
    num = int(input("Введите границу списка: "))
    num_list = [i for i in range(1, num + 1)]
    print(num_list)
    reverse_list = copy.deepcopy(num_list)
    reverse_list.sort(reverse=True)
    print(reverse_list)
    my_dict = dict(zip(num_list, reverse_list))
    print(my_dict)
except ValueError:
    print("Ошибка: вы ввели не целое число или текст!")
