items = [2, 4, 6]
result = []
for item in items:
    if item % 4 == 0:
        continue
    result.append(item * 2)
print(result)

resources = [
    {"name": "Laptop", "available": 0},
    {"name": "Mouse", "available": 0},
    {"name": "Keyboard", "available": 3}
]
resources = [ 
    resource for resource in resources
    if resource["available"] > 0
]
print(resources)

transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

def total_quantity_per_fellow(transactions):
    totals = {}

    for transaction in transactions:
        fellow = transaction["fellow"]
        quantity = transaction["quantity"]

        if fellow not in totals:
            totals[fellow] = 0

        totals[fellow] += quantity

    return totals
result = total_quantity_per_fellow(transactions)
print(result)

