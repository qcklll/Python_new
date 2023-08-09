from random import *

first_list = [randint(1,10) for _ in range(4)]
second_list = [randint(11,20) for _ in range(7)]
print(first_list)
print(second_list)
third_list= []
"""step = len(second_list)"""
step = len(second_list)
print(step)

for k in range(len(first_list) + len(second_list)):
    if k < len(first_list):
        third_list.append(first_list[k])
    if k < len(second_list):
        third_list.append(second_list[k])

print(third_list)
