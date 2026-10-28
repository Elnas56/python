def count_occurrences(numbers, target):
    if not numbers:
        return 0
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count
print(count_occurrences([2, 5, 2, 8, 2], target = 2))
print(count_occurrences([1, 4, 7], target = 10))                