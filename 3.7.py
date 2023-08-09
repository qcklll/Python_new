'''
def prog(my_list,):
    element = (max(my_list))
    index = my_list.index(element)
    maksimum = [element, index]
    return maksimum
prog([1,3,4,5,6])
a = maksimum
print(a)
'''
def prog(my_list):
    element = max(my_list)
    index = my_list.index(element)
    maksimum = [element, index]
    return maksimum

my_list = [1, 3, 4, 5, 6]
a = prog(my_list)
print(a)
