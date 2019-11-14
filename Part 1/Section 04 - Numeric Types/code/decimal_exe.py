import decimal
from decimal import Decimal


def addnumbers(additions):
    result = 0
    for i in range(additions):
        result += number
    return result


x = Decimal('1.25')
y = Decimal('1.35')

with decimal.localcontext() as ctx:
    ctx.prec = 6
    ctx.rounding = decimal.ROUND_HALF_UP
    number = Decimal(value='10.01')
    print(addnumbers(10000))
    print(round(x, 1))
    print(round(y, 1))


print(round(x, 1))
print(round(y, 1))
