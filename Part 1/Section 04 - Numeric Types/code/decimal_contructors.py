import decimal
from decimal import Decimal


a = Decimal((0, (1, 2, 3, 4), -7))
b = Decimal('-3.142')
print(a)
print(b)
print(type(a), type(b))


# Avoid using floats in using Decimal constructors



with decimal.localcontext() as ctx:
    