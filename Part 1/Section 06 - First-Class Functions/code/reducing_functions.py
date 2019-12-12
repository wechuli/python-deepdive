max([1, 2, 3, 4])

print(max([1, 2, 3, 4]))

my_list = [5, 6, 8, 10, 0, 9]


def max_value(a, b):
    return a if a > b else b


def min_value(a, b):
    return a if a < b else b


def add_values(a, b):
    return a+b


# def max_sequence(sequence):
#     result = sequence[0]
#     for e in sequence[1:]:
#         result = max_value(result, e)
#     return result


def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result


# print(max_sequence([234, 43, 22, 23, 4344, 2, 12, 3, -454343, 22, 0]))

print(_reduce(min_value, my_list))
print(_reduce(max_value, my_list))
print(_reduce(add_values, my_list))
