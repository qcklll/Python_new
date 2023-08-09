def nechet(numbers):
    num_nechet = 0

    for num in numbers:
        if num %2!= 0:
            num_nechet += num       
    return num_nechet
        

    

numbers = [15, 3, 11, 6, 1, 4]
result = nechet(numbers)
print(result)
    
        
