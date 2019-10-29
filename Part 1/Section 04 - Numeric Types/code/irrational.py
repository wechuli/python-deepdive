import math
from fractions import Fraction

x = Fraction(math.pi)
x.limit_denominator(10)
print(x)
