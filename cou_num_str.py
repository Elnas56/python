word = "programming"
character = 'g'
count = 0
for i in word:
    if i == character:
        count+=1
print(count)

properties = ["available", "sold", "available", "sold", "available"]
status = "available"
count = 0
for property_status in properties:
    if property_status == status:
        count += 1
print(count)

