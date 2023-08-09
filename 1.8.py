n = int(input("Введите ваше число для вычисления Фибоначчи"))
fibo = [1,1]
for k in range(2,n+1):
    fibo.append(fibo[k-1] + fibo[k-2])
print(fibo)
    
