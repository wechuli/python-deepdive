
from functools import wraps


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            print(
                f"decorated function called a = {self.a}, b = {self.b}")
            return fn(*args, **kwargs)
        return inner


@MyClass(10, 20)
def my_func(s):
    print(f'Hello {s}')


my_func('Wechuli')
# or

obj = MyClass(10, 20)
@obj
def my_func2(s):
    print(f'Hello {s}')


my_func2('Wechuli')
