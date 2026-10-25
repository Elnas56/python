#while loops
reviews_remaining = 3

while reviews_remaining > 0:
    print("Reviewing a property...")
    reviews_remaining = reviews_remaining - 1

print("All properties reviewed.")

#What will the exact output be?
#How many times will the while loop execute?
#Why does the loop eventually stop?
count = 1

while count <= 3:
    print(count)
    count = count + 1

print("Finished")

#Spot the infinite loop
count = 1

while count <= 3:
    print(count)

#Which property names will print?
#How many times will the while loop run?
#What will the final value of count be?
#Why must index = index + 1 be inside the while loop?
properties = [
    {"name": "Atlantic Tower", "price": 30000000},
    {"name": "Happy Estate", "price": 25000000},
    {"name": "Elegant Havana", "price": 50000000},
    {"name": "Greener Pasture", "price": 40000000}
]

count = 0
index = 0

while index < len(properties):
    if properties[index]["price"] < 40000000:
        print(properties[index]["name"])
        count = count + 1

    index = index + 1

print(f"Total affordable properties: {count}")

#What happens when the loop reaches Elegant Havana, 
#whose price is ₦50 million? Think about whether index will increase when the if condition is false.
while index < len(properties):
    if properties[index]["price"] < 40000000:
        print(properties[index]["name"])
        count = count + 1
        index = index + 1

properties = [
    {"name": "Atlantic Tower", "price": 30000000},
    {"name": "Happy Estate", "price": 25000000},
    {"name": "Elegant Havana", "price": 50000000},
    {"name": "Greener Pasture", "price": 40000000}
]

budget = 40000000
for property in properties:
    if property["price"] <= budget:
        print(property["price"])
        count = count + 1
    print(count)    

1) Atlantic Tower
Happy Estate
Greener Pasture

2) 3

3)this is because it tells us that our count is starting for zero