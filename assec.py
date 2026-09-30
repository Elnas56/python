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