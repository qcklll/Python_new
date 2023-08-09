txt = input("Введите текст: ")


mal_a=ord("а")
big_a=ord("А")
mal_ya=ord("я")
big_ya=ord("Я")



for k in txt:
    s = ord(k)
    if s >= mal_a and s <= mal_ya:
        s -= 32
        print(chr(s), end = "")
    elif s >= big_a and s <= big_ya:
        s +=32
        print(chr(s), end = "")
    else:
        print(k, end="")
        

      
