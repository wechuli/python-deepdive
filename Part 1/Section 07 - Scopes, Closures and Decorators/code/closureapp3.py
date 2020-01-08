def counter(initial_value: float = 0):
    def inc(increment: float = 1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc


counter1 = counter()
print(counter1())
print(counter1())


def funct_counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f'{fn.__name__} has been called {cnt} times')
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


counter_add = funct_counter(add)
counter_mul = funct_counter(mult)

counter_add(12, 485)
counter_mul(43, 93)
counter_add(12, 34)
