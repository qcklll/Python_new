n = 50
E = set(range(1, n+1))
A = {s for s in E if s%3==0}
B = {s for s in E if s%4==0}
N = (A|B - A&B)
print(N)
