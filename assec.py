def ticket_total(price, quantity):
    total = price * quantity
    return total

amount = ticket_total(7, 3)
print(amount)

def passing_scores(scores):
    passed = []

    for score in scores:
        if score >= 50:
            passed.append(score)

    return passed

print(passing_scores([49, 50, 80, 65]))

def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = profile["tags"].copy()
    updated["tags"].append(tag)
    return updated

original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]

changed["tags"].append("debugging")

assert original["tags"] == ["python"]
print(changed["tags"])

def summarise_amounts(raw_values):
    total = 0
    rejection = 0
    for raw in raw_values:
        try: 
            amount = int(raw)
        except ValueError:
            rejected += 1
            continue
        if amount >= 0:
            total += amount
        else:
            reject += 1
    return {"total": total, "rejected": rejected}
#print(summarise_amounts["10", " 5 ", "bad", "-3", "0", ""])

def reserve_stock(stock, order):
    remaining = stock.copy()

    for item, quantity in order:

        if item not in remaining:
            raise ValueError("Unknown item")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > stock[item]:
            raise ValueError("Insufficient stock")

            remaining[item] -= quantity
    return remaining


