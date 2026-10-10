#Declaring a function
def greet_student(name):
    return "Welcome, " + name
message = greet_student("Ada")
print(message)

#A function can calculate something and return its result to the caller.
def multiply(a, b):
    return a * b
answer = multiply(4, 3)
print(answer)

#Write a function named calculate_ticket_cost that:
#1. Accepts two parameters: cost_per_item and quantity.

def calculate_ticket_cost(cost_per_item, quantity):
    return cost_per_item * quantity
total_cost = calculate_ticket_cost(2500, 4)
print(total_cost)

def find_student(students, student_name):
    for student in students:
        if student == student_name:
            return student
    return None



