from functools import partial


def my_func(a, b, c):
    print(a, b, c)


def f(x, y):
    return my_func(10, x, y)


my_func(10, 20, 30)
f(20, 30)

f_partial = partial(my_func, 10)

f_partial(56, 45)


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)


my_func(10, 20, 100, 200, 300, k1='a', k2='b', another=[123, 434], anoth="ff")

my_func_partial = partial(my_func, 10, k1='k1-changed', verse="poem")

my_func_partial(20, 100, 45, k2='k2-previous')
