from functools import reduce


def max_value(a, b):
    return a if a > b else b


def min_value(a, b):
    return a if a < b else b


def add_values(a, b):
    return a+b


my_list = [8, 10, 6, -554, 0, 9]
my_set = {1, 244, 3, 4, 0, 5}

print(reduce(max_value, my_list))
print(reduce(min_value, my_set))


print(any(my_set))
print(all(my_set))
