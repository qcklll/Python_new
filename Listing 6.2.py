def show(L, symb):
    for s in L:
        print(symb, s, sep="", end="")

    print(symb)

D = {"A":1,"B":2,"C":3}

show(D.values(), "#")

def get_symbs(n):
    if n>10 or n<1:
        num=10
    else:
        num=n
    S=set()
    Nmin=ord("A")
    Nmax=ord("Z")
    while len(S)<num:
        S.add(chr(randint(Nmin, Nmax)))
    return S
