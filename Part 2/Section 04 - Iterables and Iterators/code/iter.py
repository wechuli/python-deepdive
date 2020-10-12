l = [1, 2, 3, 4]

l_iter = iter(l)
print(type(l_iter))


class Squares:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2


sq = Squares(5)


for i in sq:
    print(i)


sq_iter = iter(sq)
print('__next__' in dir(sq_iter))


class SquaresIterator:
    def __init__(self, squares):
        self._squares = squares
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._squares):
            raise StopIteration
        else:
            result = self._squares[self._i]
            self._i += 1
            return result


sq_iterator = SquaresIterator(sq)
print(sq_iterator.__next__())
print(sq_iterator.__next__())


class SimpleIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'Nope'


print('__iter__' in dir(SimpleIter()))

# best way to check it to call iter()

# look before you leap
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# ask for forgiveness later, try to iterate then catch the error