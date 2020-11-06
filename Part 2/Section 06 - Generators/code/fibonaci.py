from timeit import timeit
from functools import lru_cache


@lru_cache()
def fib_recursive(n):
    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_standard(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1

    return fib_1


class FibIter:

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = fib_standard(self.i)
            self.i += 1
            return result

# fibonaci using generators


def fib_nonrecursive_gen(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


for f in fib_nonrecursive_gen(7):
    print(f)

# compare fib calulated by iterator vs generator


iterator_fib = timeit('list(FibIter(5000))', globals=globals(), number=1)
generator_fib = timeit(
    'list(fib_nonrecursive_gen(5000))', globals=globals(), number=1)


print(f' Iterator: {iterator_fib}, Generator: {generator_fib}')
