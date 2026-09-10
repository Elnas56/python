property_name = "Fortune crest"
location = "Uke, Karu"
price = 4000000
plot_size = "500sqm"  

client_name = input("Enter client's name:")
number_of_plots = int(input("How many plots do you want? "))

total_price = price * number_of_plots
print("Total Price:", total_price)

properties = [
    "Fortune crest",
    "Hutu Prestige",
    "Moon Valley",
    "Moontech Peninsula."
]

for property in properties:
    print(property)

property = {
    "name": "Fortune Crest",
    "location": "Uke, Karu",
    "price": 4000000,
    "plot_size": "500sqm",
    "status": "available"
}

properties = [
    {
        "name": "Hutu Prestige",
        "location": "Before Centenary City, Airport Road, Abuja",
        "price": 48600000,
        "plot_size": "500sqm",
        "status": "available"
    },
    {
        "name": "Moon Valley",
        "location": "Apo Tafyi, Abuja",
        "price": 32500000,
        "plot_size": "500sqm",
        "status": "available"
    },
    {
        "name": "Moon Tech Peninsula",
        "location": "Ketti, Kabusa Abuja",
        "price": 15000000,
        "plot_size": "500sqm",
        "status": "available"
    }    
]

if property == "Available":
    print("This property is available for sale.")
else:
    print("Sorry, this property has been sold.")

plot_dimensions = (50, 100)

print("Plot width:", plot_dimensions[0])
print("Plot length:", plot_dimensions[1])

def calculate_total(price, plots):
    return price * plots

total = calculate_total(5000000, 2)
print("Total:", total)








