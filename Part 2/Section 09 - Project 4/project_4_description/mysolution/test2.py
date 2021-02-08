from itertools import groupby


l = ['a', 'b', 'c', 'c', 'd']

make_groups = groupby(l, lambda x: x)

print(list(make_groups))
