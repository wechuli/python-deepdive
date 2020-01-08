counters = dict()


def counter(fn):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        global counters
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


c = dict()


def counter_v2(fn, counters):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner


def add(a, b):
    return a + b


def mult(a, b):
    return a * b


counter_add = counter(add)
counted_mult = counter(mult)

counter_add(10, 20)
print(counters)
counter_add(20, 3)
print(counters)
counted_mult(1, 2)
print(counters)


counter_add_v2 = counter_v2(add, c)
counted_mult_v2 = counter_v2(mult, c)

counter_add_v2(10, 20)
print(c)
counter_add_v2(20, 3)
print(c)
counted_mult_v2(1, 2)
print(c)
