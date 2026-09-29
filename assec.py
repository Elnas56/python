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