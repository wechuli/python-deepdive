class Squares:
    def __init__(self, length: int):
        self._length = length
        self._i = 0

    def __len__(self):
        return self._length

    def __next__(self):
        if self._i >= self._length:
            raise StopIteration
        result = self._i ** 2
        self._i += 1
        return result

    def __iter__(self):
        return self


for i in Squares(4):
    print(i)

iter
print(list(enumerate(Squares(6))))

print(sorted(Squares(10), reverse=True))


