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