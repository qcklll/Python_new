def alpha():
    print("Это Alpha!")
def bravo():
    print("Это Bravo!")
def hello():
    print("А это Hello")

num = 123

print("Сначала было так: ")
alpha()
bravo()
hello()
print("num =", num)

alpha, bravo=bravo, alpha
num = hello
hello = 321

print("А стало так: ")
alpha()
bravo()
num()
print("hello =", hello)
