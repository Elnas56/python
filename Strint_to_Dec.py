import decimal
string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))

from decimal import Decimal
price = Decimal('19.99')
print(price)

import decimal
price = '25000000'
price_decimal = decimal.Decimal(price)
print(price_decimal)

import decimal
price1 = decimal.Decimal('25000000')
price2 = decimal.Decimal('15000000')
total = price1 + price2
print(total)

from decimal import Decimal
property_price = Decimal('50000000')
commission_rate = Decimal('0.05')
commission = property_price * commission_rate
print(commission)

print(type("Hello"))
print(type(50))
print(type(10.5))
print(type(Decimal('10.5')))

from  decimal import Decimal
price = input("Enter property price: ")
price = Decimal(price)
print(type(price))