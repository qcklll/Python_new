def mysum(*a):

    txt = ["чисел","квадратов","кубов"]

    def calc(n):
        s=0
        for m in range(len(a)):
            s+=a[m]**n
        return s

    for k in range(len(txt)):
        print("Сумма", txt[k]+":", calc(k+1))


mysum(1,3,5,7)
