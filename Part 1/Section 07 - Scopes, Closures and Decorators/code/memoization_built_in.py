from functools import lru_cache


@lru_cache(maxsize=8)
def fib(n):
    print(f"Calculating fib({n})")
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(16))
