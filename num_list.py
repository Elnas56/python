def find_number(numbers, target):
    i = 0
    while i < len(numbers):
         if numbers[i] == target:  
            return i
         i += 1
    return -1                      

# Test cases
print(find_number([10, 25, 30, 45], target=30))  
print(find_number([5, 8, 5, 9], 5))              
print(find_number([10, 20, 30], 99))        
