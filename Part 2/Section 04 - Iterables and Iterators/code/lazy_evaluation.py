import math


class Circle:
    def __init__(self, radius: float):
        self.radius = radius
        self._area = None

    def __repr__(self):
        return f'Radius:{self.radius}, Area:{self.area}'

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)
        return self._area


class Factorials:
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        return self.FactIter(self.length)

    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result


facts = Factorials(5)
print(list(facts))
