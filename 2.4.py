num_list_1 = [1,2,5,5]
num_list_2 = [1,2,5,5]

if len(num_list_1) == len(num_list_2) and num_list_1 == num_list_2: 
    for i in range(len(num_list_1)):
        if num_list_1[i] != num_list_2[i]:
            break
    else:
        print("Списки одинаковые")
else:
    print("Списки разные")
    
