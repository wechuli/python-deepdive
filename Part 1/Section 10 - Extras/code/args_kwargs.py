from operator import mul
from functools import reduce


def audit(fn):
    def inner(*args, **kwargs):
        print(f'Called {fn.__name__}')
        return fn(*args, **kwargs)

    return inner


@audit
def say_hello(name):
    return f'Hello {name}'


@audit
def product(*values):
    return reduce(mul, values)


print(product(1, 2, 3, 4))


class Person:
    def __init__(self, name, age, **custom_attributes):
        self.name = name
        self.age = age
        for attr_name, attr_value in custom_attributes.items():
            setattr(self, attr_name, attr_value)
