class CyclicIterator:
    def __init__(self, lst):
        self._lst = lst
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self._lst[self._i % len(self._lst)]
        self._i += 1
        return result


iter_cycle = CyclicIterator('NSWE')

numbers = range(10)

elements = list(zip(list(numbers), iter_cycle))

print(elements)


n = 10
iter_cycle = CyclicIterator('NSWE')
items = [str(i) + next(iter_cycle) for i in range(1, n+1)]
print(items)
