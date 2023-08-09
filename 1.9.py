def find_second (numbers):
    if len(numbers) < 2:
        return None
    
    
    max_number = numbers[0]
    second_number = numbers[1]

    
    for num in numbers:
        if num > max_number:
            second_number = max_number
            max_number = num
        elif num > second_number:
            second_number = num
    return second_number

numbers = [5, 15, 25, 7, 1, 16]
result = find_second(numbers)
print(result)

    
