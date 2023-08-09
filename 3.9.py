from random import randint, seed

seed(5)

random_list = [randint(1,23) for _ in range(10)]
new_list = []
print(random_list)
for i in range(len(random_list)):
    new_list.append(random_list[i])
    if i < len(random_list) - 1:
        new_element = random_list[i] + random_list[i+1]
        new_list.append(new_element)

print(new_list)
