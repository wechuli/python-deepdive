

# def fib(n):
#     print(f"Calculating fib({n})")
#     return 1 if n < 3 else fib(n+1) + fib(n-2)

# Using a class
class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print(f'Calculating fib({n})')
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]


f = Fib()
print(f.fib(10))

# Using a Closure


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print(f'Calculating fib({n})')
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib


f_closure = fib()
print(f_closure(10))
