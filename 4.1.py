from random import *

count = 15
A = set()
B = set()
while len(A) < count - 10:
    A.add(randint(1,10))

while len(B) < count - 5:
    B.add(randint(10,30))

print(A.union(B))

