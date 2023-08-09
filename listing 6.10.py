def myfunction():
    global A, B

    A="Альфа"
    B="Браво"
    D="Дельта"

    print("В функции: A=", A)
    print("В функции: B=", B)
    print("В функции: C=", C)
    print("В функции: D=", D)

A="Alpha"
C="Charlie"
D="Delta"

print("До вызова функции: A =", A)
print("До вызова функции: C =", C)
print("До вызова функции: D =", D)

myfunction()

print("После вызова функции: A =", A)
print("После вызова функции: B =", B)
print("После вызова функции: C =", C)
print("После вызова функции: D =", D)
