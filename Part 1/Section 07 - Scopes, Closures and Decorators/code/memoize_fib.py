def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memoize
def fib(n):
    print(f"Calculating fib({n})")
    return 1 if n < 3 else fib(n-1) + fib(n-2)


@memoize
def fact(n):
    print(f"Calculating factorial of {n}")
    return 1 if n < 2 else n * fact(n-1)


print(fib(10))
print(fib(11))
print(fact(5))
