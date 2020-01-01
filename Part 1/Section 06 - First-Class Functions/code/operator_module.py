from operator import add, mul, pow, mod, floordiv, neg, lt, le, gt, ge, eq, ne, is_, is_not, and_, not_, truth, concat, contains, countOf, getitem, setitem, delitem, itemgetter, attrgetter, methodcaller
from functools import reduce


print(add(23, 10))
print(mul(10, 10))
print(reduce(mul, [1, 2, 3, 4, 5]))

mylist = [1, 2, 3, 4]
print(getitem(mylist, 3))
