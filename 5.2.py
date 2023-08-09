B = "{0: {2}{1}}"
num = 6
for k in range(num):
    print(B.format("*", num-k, ">"), end="")
    print(" "*2*(k+1), end="")
    print(B.format("*", k ,"<"))
    
