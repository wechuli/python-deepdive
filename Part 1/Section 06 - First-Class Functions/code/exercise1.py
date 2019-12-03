from random import random
from math import floor


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(numbers, key=lambda number: random()))
