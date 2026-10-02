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

def order_food('JollofRice', '2', Large)

