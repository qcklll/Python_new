def mysum(n):
    if n==0:
        return 0;
    else:
        return n+mysum(n-1)

for k in range(3):
    print(mysum(k), end = " ")

print()

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for k in range(15):
    print(fib(k+1), end=" ")
