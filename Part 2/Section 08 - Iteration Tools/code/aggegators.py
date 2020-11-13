def squares(n):
    for i in range(n):
        yield i ** 2


print(max(squares(6)))
print(min(squares(6)))
print(sum(squares(6)))


print(bool(0+6j))
print(bool([]))


class Person:
    def __init__(self):
        self.i = 0

    def __bool__(self):
        return False


class MySeq:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self):
        pass




person = Person()

print(bool(person))


print(any([0, '', None, (12,)]))
print(all([10, 'hello']))
