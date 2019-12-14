from functools import reduce


def multiply(a, b):
    return a*b


my_iterable = [1, 2, 3, 4]

print(reduce(multiply, my_iterable))

gen = (x*2 for x in range(10))
print(max(gen))
