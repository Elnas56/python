numberList = [12, 3, 55, 23, 6, 78, 33, 4]
max = numberList[0]
for num in numberList:
    if max < num:
        max = num
print(max)

numberList = [12, 3, 55, 23, 6, 78, 33, 4]
largest = numberList[0]
for num in numberList:
    if largest < num:
        largest = num
print(largest)

property_prices = [25000000, 45000000, 18000000, 70000000, 35000000]
largest = property_prices[0]
for num in property_prices:
    if largest < num:
        largest = num
print(largest)        