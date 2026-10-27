def find_number(numbers, target):
    
    hen = 0
    while hen < len(numbers): 
        
        if numbers(hen) == target:
        
            return hen
        
        hen += 1
    
    return -1
print(find_number([10, 25, 30, 45], 30))           
#print(find_number([5, 8, 5, 9], 5))
#print(find_number([10, 20, 30], 99))