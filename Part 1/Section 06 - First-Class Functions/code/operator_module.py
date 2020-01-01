from operator import add, mul, pow, mod, floordiv, neg, lt, le, gt, ge, eq, ne, is_, is_not, and_, not_, truth, concat, contains, countOf, getitem, setitem, delitem, itemgetter, attrgetter, methodcaller
from functools import reduce


print(add(23, 10))
print(mul(10, 10))
print(reduce(mul, [1, 2, 3, 4, 5]))

mylist = [1, 2, 3, 4]
print(getitem(mylist, 3))


f_getter = itemgetter(2)
print(f_getter(mylist))


class MyClass:
    def __init__(self):
        self.a = 10000
        self.b = 20
        self.c = 30

    def test(self):
        print("Test method running")


obj = MyClass()

f_attrgetter = attrgetter('a')
print(f_attrgetter(obj))
