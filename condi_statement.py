budget = 40000000
property_price = 45000000

if budget > property_price:
    print("You have enough money")
elif budget == property_price:
    print("Your budget exactly matches the price")
else:
    print("You need more money")

budget = 45000000
property_price = 45000000

if budget > property_price:
    print("You have enough money")
elif budget == property_price:
    print("Your budget exactly matches the price")
else:
    print("You need more money")

budget = 50000000
property_price = 45000000
location_matches = False

if budget >= property_price:
    if location_matches:
        print("Recommend this property")
    else:
        print("Property is affordable but in the wrong location")
else:
    print("Property is over budget")

budget = 30000000
property_price = 45000000
location_matches = True

if budget >= property_price:
    if location_matches:
        print("Recommend this property")
    else:
        print("Property is affordable but in the wrong location")
else:
    print("Property is over budget")