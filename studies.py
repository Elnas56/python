age = int(input("Enter your age: "))

while age != 0:
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

    age = int(input("Enter your age (0 to quit): "))

topping = ""

while topping != "quit":
    topping = input("Enter a pizza topping: ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")

sandwich_orders = ['tuna', 'egg', 'friut', 'veggies']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich} sandwich.")
    
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:

    print(sandwich)

sandwich_orders = ['pastrami', 'tuna', 'egg', 'pastrami', 'friut', 'veggies', 'pastrami']

finished_sandwiches = []

print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich} sandwich.")
    
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)

responses = {}

while True:
    name = input("\nWhat your name? ")
    
    place = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = place
    
    another = input("Would you like another person to respond? (yes/ no) ")
    
    if another == 'no':
        break

print("\n--- Dream Vacation Poll Results ---")

for name, place in responses.items():
    print(f"{name} would like to visit {place}.")

