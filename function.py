def greet_user():
    print("Hello!")

greet_user()

def greet_user(username):
    print("Hello, " + username.title() + "!")

greet_user('jesse')

def display_message():
    print("I am learning about functions in Python.")

display_message()    

def faviourite_book(title):
    print(f"One of my favourite books is {title}.")

faviourite_book('Alice in Wonderland')
faviourite_book("Things Fall Apart")
faviourite_book("THe Hobbit")

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie') 

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')

def make_shirt(size, message):
    print("The shirt of the size " + size  + " and has the message " + message + " printed.")
make_shirt('Large', 'I love Python')
make_shirt(size='Medium', message='Python is fun')

def make_shirt(size='Large', message='I love Python'):
    print("The shirt of the size " + size + " and has the message " + message + " printed on it.")
make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Python is intresting')


def describe_city(city, country='iceland'):
    print(city.title() + " is in " + country.title())
describe_city('reykjavik')
describe_city('abuja', 'nigeria')
describe_city('Paris', 'France')

def order_food(food, quantity, size):
    print(f"You ordered {quantity} {size} portions of {food}.")
order_food('jollof Rice', '2', 'large')

def order_food(food='Jollof Rice', quantity='3', size='medium'):
    print(f"You ordered {quantity} {size} portions of {food}.")
order_food()

def ready_food(customer_name, food, quantity):
    print(f"{customer_name} ordered {quantity} portions of {food}.")
ready_food('Joy', 'beans', '2')

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

'''def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")'''

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

def city_country(name_city, name_country):
    vacation =  name_city + ' ' + name_country
    return vacation.title()
trip = city_country('santiago', 'chile')
print(trip)

def city_country(name_city, name_country, place):
    vacation =  name_city + ' ' + name_country
    return vacation.title()
trip = city_country('santiago chile', 'nigeria abuja', 'india mubui')
print(trip)

def greet_user(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'try', 'margot']
greet_user(usernames)