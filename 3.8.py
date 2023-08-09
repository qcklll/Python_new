'''
from random import randint

random_list = [randint(1,47) for _ in range(1,21)]
print(random_list)

chet_chisla=[]
nechet_chisla=[]

for i in random_list:
    if i%2==0:
        chet_chisla.append(i)
    else:
        nechet_chisla.append(i)

random_list = chet_chisla + nechet_chisla
print(random_list)
'''
from random import randint

random_list = [randint(1, 47) for _ in range(20)]
print(len(random_list))

chet_chisla = random_list[::2]  # Срез для получения элементов с четными индексами
nechet_chisla = random_list[1::2]  # Срез для получения элементов с нечетными индексами

chet_chisla.sort()  # Сортировка элементов с четными индексами по возрастанию
nechet_chisla.sort(reverse=True)  # Сортировка элементов с нечетными индексами по убыванию

random_list = chet_chisla + nechet_chisla  # Объединение сортированных срезов в итоговый список
print(random_list)
