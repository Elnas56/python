import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

from decimal import Decimal
number = Decimal(0.1)
print(number)


from decimal import Decimal
number = Decimal("0.1")
print(number)

from decimal import Decimal
a = Decimal("10.50")
b = Decimal("5.25")
print(a + b)

from decimal import Decimal
a = Decimal("10.50")
b = Decimal("5.25")
print(a - b)

from decimal import Decimal
a = Decimal("10.50")
b = Decimal("5.25")
print(a * b)

from decimal import Decimal
a = Decimal("10.50")
b = Decimal("5.25")
print(a / b)

from decimal import Decimal
a = Decimal("10")
b = Decimal("10.50")
c = Decimal("-50.75")

print(type(a))
print(type(b))
print(type(c))

land_price = 2500000.50
from decimal import Decimal
land_price = Decimal("2500000.50")
deposit = Decimal("500000.00")
balance = land_price - deposit
print(balance)

land_price = Decimal("2500000.00")
development_fee = Decimal("150000.00")
legal_fee = Decimal("100000.00")
total = land_price + development_fee + legal_fee
print(total)

from decimal import Decimal
balance = Decimal("100000.50")
deposit = Decimal("25500.25")
new_balance = balance + deposit
print(new_balance)

land_price = 5500000.00
legal_fee = 150000.00
Documentation = 100000.00
Development_fee = 250000.00

from decimal import Decimal
land_price = Decimal("5500000.00")
legal_fee = Decimal("150000.00")
documentation = Decimal("100000.00")
development_fee = Decimal("250000.00")
total = land_price + legal_fee + documentation + development_fee
print(total)

Rice = 25500.50
Oil = 8250.25
Milk = 3100.75

from decimal import Decimal
rice = Decimal("25500.50")
oil = Decimal("8250.25")
milk = Decimal("3100.75")
total = rice + oil + milk
print(total)

from decimal import Decimal
amount = Decimal("5000.00")
fee = Decimal("25.50")
total = amount + fee
print(total)

Basic_salary = 250000.00
Transport = 50000.00
Housing = 100000.00
Tax_deduction = 20000.50

from decimal import Decimal
basic_salary = Decimal("250000.00")
transport = Decimal("50000.00")
housing = Decimal("100000.00")
tax_deduction = Decimal("20000.50")

gross = basic_salary + transport + housing
net = gross - tax_deduction
print("Gross:", gross)
print("Net:",net) 

Units_used = 125.5
Price_per_unit = 75.25

from decimal import Decimal
units_used = Decimal("125.5")
price_per_unit = Decimal("75.25")
bill = units_used * price_per_unit
print(bill)

property_cost = 10000000
discount_rate = 0.05

from decimal import Decimal
price = Decimal("10000000")
discount_rate = Decimal("0.05")

discount = price * discount_rate
final_price = price - discount

print("Discount:", discount)
print("Final price:", final_price)


