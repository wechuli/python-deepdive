import math


class FactorialIter:
    def __init__(self, n):
        self._n = n
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self._n:
            raise StopIteration
        else:
            result = math.factorial(self._i)
            self._i += 1
            return result


def fact():
    i = 0

    def inner():
        nonlocal i
        result = math.factorial(i)
        i += 1
        return result
    return inner


fact_iter = iter(fact(), math.factorial(5))
factorial_iter = FactorialIter(5)

for i in factorial_iter:
    print(i)
