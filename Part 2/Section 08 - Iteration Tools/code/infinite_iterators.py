from itertools import count, cycle, repeat, islice
from decimal import Decimal

g = count(10)

print(list(islice(g, 5)))

# Count can take flots as well

g = count(1, 0.04)
print(list(islice(g, 6)))


g = count(Decimal('1'), Decimal('0.04'))
print(list(islice(g, 6)))

# cycles

cyc = cycle(('red', 'green', 'red', 'grren'))

print(list(islice(cyc, 10)))
