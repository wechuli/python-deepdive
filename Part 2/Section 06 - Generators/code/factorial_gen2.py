import math


def fact(n):
    for i in range(n):
        yield math.factorial(i)


gen = fact(5)

for i in gen:
    print(i)


def squares(n):
    for i in range(n):
        yield i ** 2
