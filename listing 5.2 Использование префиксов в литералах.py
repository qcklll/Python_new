A="\"Java\"n\"Python\""
print(A)
print("Simvolov:", len(A))

B=r"\"Java\"\n\"Python\""
print(B)
print("Simvolov:", len(B))

name="Python"
C=f"Yazik {name} - prostoi i ponyatni"
print(C)
C=f"Yazik {name!r} - prostoi i ponyatni"
print(C)

num=12.34567

txt=f"Chislo: {num:9.3f}"
print(txt)
txt=f"Chislo: {num:09.3f}"
print(txt)

num=42
txt=f"Chislo: {num:*>9d}"
print(txt)

txt=f"Chislo: {num:#09x}"
print(txt)
txt=f"Chislo: {num:9x}"
print(txt)
txt=f"Chislo: {num:*<9x}"
print(txt)

txt=f"Chislo: {num:*^#09o}"
print(txt)

txt=f"Chislo: {num:9b}"
print(txt)
