from itertools import islice
import math
import random


l = [1, 2, 3, 4]

result = islice(l, 0, 3)
print(list(result))


def factorials(n):
    for i in range(n):
        yield math.factorial(i)


result = islice(factorials(10), 0, 5)

print(list(result))


result = islice(factorials(100), 2, 40, 4)
print(list(result))
