budget_text = input("Enter your budget: ")

try:
    budget = int(budget_text)

    if budget <= 0:
        print("Budget must be greater than zero.")
    else:
        print(f"Your budget is ₦{budget}")

except ValueError:
    print("Please enter a whole number.")