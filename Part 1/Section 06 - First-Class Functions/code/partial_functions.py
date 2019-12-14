from functools import partial


def my_func(a, b, c):
    print(a, b, c)


def f(x, y):
    return my_func(10, x, y)


my_func(10, 20, 30)
f(20, 30)
