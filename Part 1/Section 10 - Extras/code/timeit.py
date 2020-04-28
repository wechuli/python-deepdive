from timeit import timeit


def outer(fn):
    def inner(*args, **kwargs):
        return fn(*args, **kwargs)
    return inner


@outer
def add(a: float, b: float) -> float:
    return a + b


print(timeit(stmt="math.sqrt(2)", setup='import math'))
print(timeit(stmt="sqrt(2)", setup="from math import sqrt"))
