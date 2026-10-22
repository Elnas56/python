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

