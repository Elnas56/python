#find the largest number in a list.
def find_largest(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
result = find_largest([3, 41, 56, 21, 76, 9])
print(result)

def find_largest(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
result = find_largest([-10, -5, -2, -18])
print(result)

def find_largest(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
result = find_largest([])
print(result)


