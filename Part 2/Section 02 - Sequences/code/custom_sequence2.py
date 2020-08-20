from functools import lru_cache


class Fibonaci:
    def __init__(self, n: int) -> None:
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s: int or slice) -> int:
        if isinstance(s, int):
            if s < 0:
                s = self.n + s
            if s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fibonaci._fib(s)
        else:
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [Fibonaci._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2*10)
    def _fib(n: int) -> int:
        if n < 2:
            return 1

        else:
            return Fibonaci._fib(n-1) + Fibonaci._fib(n-2)


f = Fibonaci(8)

print(f[2])
print(list(f))
print(f[-2])


f = Fibonaci(10)
print(f[4:1:-1])
