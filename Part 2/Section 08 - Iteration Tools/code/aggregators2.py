from numbers import Number

print(isinstance(12.2, Number))

l = [10, 20, 30, 40, 's']


is_all_numbers = all(isinstance(number, Number) for number in l)

def is_numeric(v):
    return isinstance(v,Number)

print(is_all_numbers)


pred_l = map(is_numeric,l)
