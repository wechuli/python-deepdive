from functools import wraps
from inspect import signature


def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{fn.__name__} was called {count} times")
        return fn(*args, **args)

    return inner


@counter
def mult(a: int, b: int, c: int = 1):
    """
    returns the product of three variables
    """
    return a*b*c


print(mult.__name__)
print(mult.__code__.co_freevars)
print(help(mult))
print(signature(mult))
