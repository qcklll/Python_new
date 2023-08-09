import random

def create_nested_list(m, n):
    nested_list = [['' for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            random_letter = chr(random.randint(65, 90))  # случайная заглавная буква
            nested_list[i][j] = random_letter
    return nested_list

result = create_nested_list(3, 5)
print(result)
