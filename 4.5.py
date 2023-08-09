from random import randint, seed
seed(2019)

nechet_len = []

nechet_chisla = [randint(1,25) for k in range(1,14) if k%2==0]
print(nechet_chisla)

for i in range(len(nechet_chisla) - 1):
    nechet_len.append((nechet_chisla[i], nechet_chisla[i+1]))

print(set(nechet_len))
