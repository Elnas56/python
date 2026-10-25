#predict the exact output.
#how many times do you think print(property_name) will execute, and why?
properties = ["Atlantic Tower", "Elegant Havana", "Happy Estate"]

for property_name in properties:
    print(property_name)

#How many times will print(property_name) execute now, and what will the last line of output be?
properties = ["Atlantic Tower", "Elegant Havana", "Happy Estate", "Greener Pasture"]

for property_name in properties:
    print(property_name)

#Using a loop with a condition
#What property names will be printed?
#How many times will the for loop iterate?
#Why won't every property name necessarily be printed?
properties = [
    {"name": "Atlantic Tower", "price": 30000000},
    {"name": "Elegant Havana", "price": 50000000},
    {"name": "Happy Estate", "price": 25000000}
]

budget = 30000000

for property in properties:
    if property["price"] <= budget:
        print(property["name"])

#What will the program print, and why?
properties = [
    {"name": "Atlantic Tower", "price": 30000000},
    {"name": "Elegant Havana", "price": 50000000},
    {"name": "Happy Estate", "price": 25000000}
]

budget = 20000000
count = 0

for property in properties:
    if property["price"] <= budget:
        count = count + 1

print(count)

#Which property names will be printed, in order?
#How many times will the for loop iterate?
#Why does a property priced exactly ₦40 million qualify?
properties = [
    {"name": "Atlantic Tower", "price": 30000000},
    {"name": "Elegant Havana", "price": 50000000},
    {"name": "Happy Estate", "price": 25000000},
    {"name": "Greener Pasture", "price": 40000000}
]

budget = 40000000
count = 0

for property in properties:
    if property["price"] <= budget:
        print(property["name"])
        count = count + 1

print(f"Total matching properties: {count}")

#Which property names will be printed, and in what order?
#How many times will the for loop iterate?
#What will the final value of count be?
#Why is Happy Estate excluded even though its price is within budget?
#Why does Greener Pasture qualify when its price is exactly ₦40 million?
properties = [
    {"name": "Atlantic Tower", "price": 30000000, "location_matches": True},
    {"name": "Elegant Havana", "price": 50000000, "location_matches": True},
    {"name": "Happy Estate", "price": 25000000, "location_matches": False},
    {"name": "Greener Pasture", "price": 40000000, "location_matches": True}
]

budget = 40000000
count = 0

for property in properties:
    if property["price"] <= budget and property["location_matches"]:
        print(property["name"])
        count = count + 1

print(f"Total matching properties: {count}")

#1. What prints on each line?
#2. What is the final value of count?
#3. Why does the first line print 0?
count = 0

for number in [10, 20, 30]:
    if number > 10:
        count = count + 1

    print(count)

#What will print, and what will the final value of count be?
count = 0

for number in [10, 20, 30]:
    if number > 10:
        count = count + 1
        print(number)

#1. Which numbers will print inside the loop?
#2. How many times will the while loop run?
#3. What is the complete output, including "Finished"?
count = 1

while count <= 4:
    if count % 2 == 0:
        print(count)
    count = count + 1

print("Finished")