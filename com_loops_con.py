#Combining loops and conditions
properties = [
    {"name": "Atlantic Tower", "price": 30000000},
    {"name": "Happy Estate", "price": 25000000},
    {"name": "Elegant Havana", "price": 50000000},
    {"name": "Greener Pasture", "price": 40000000}
]

budget = 40000000
count = 0

for property in properties:
    if property["price"] <= budget:
        print(property["name"])
        count = count + 1

print(f"Total affordable properties: {count}")

#Which property or properties will print?
#How many times will the loop run?
#What is the final value of count?
budget = 25000000
count = 0

for property in properties:
    if property["price"] <= budget:
        print(property["name"])
        count = count + 1

print(f"Total affordable properties: {count}")

properties = [
    {"name": "Atlantic Tower", "price": 30000000, "location_matches": True},
    {"name": "Happy Estate", "price": 25000000, "location_matches": False},
    {"name": "Elegant Havana", "price": 35000000, "location_matches": True},
    {"name": "Greener Pasture", "price": 40000000, "location_matches": True}
]

budget = 40000000
count = 0

for property in properties:
    if property["price"] < budget and property["location_matches"]:
        print(property["name"])
        count = count + 1

print(f"Total properties: {count}")

properties = [
    {"name": "Atlantic Tower", "price": 30000000, "location_matches": True},
    {"name": "Happy Estate", "price": 25000000, "location_matches": False},
    {"name": "Elegant Havana", "price": 35000000, "location_matches": True},
    {"name": "Greener Pasture", "price": 40000000, "location_matches": True}
]

budget = 40000000
count = 0

for property in properties:
    if property["price"] < budget and property["location_matches"]:
        print(property["name"])
        count = count + 1

print(f"Affordable properties: {count}")

if count >= 2:
    print("Good property options available.")
else:
    print("Limited property options.")

