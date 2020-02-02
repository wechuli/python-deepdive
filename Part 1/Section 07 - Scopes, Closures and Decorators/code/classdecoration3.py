
from math import sqrt
from functools import total_ordering

# total ordering monkey patches the >= , <= and ! operators


def complete_ordering(cls):

    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self, other: self < other or self == other
        cls.__gt__ = lambda self, other: not(
            self < other) and not(self == other)
        cls.__ge__ = lambda self, other: not(self < other)

    return cls


@complete_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        return NotImplemented

    # def __le__(self, other):
    #     pass

    # def __gt__(self, other):
    #     pass

    # def __ne__(self, other):
    #     pass


p1, p2, p3 = Point(2, 3), Point(2, 3), Point(100, 200)

print(p1 >= p2)
print(p1 != p2)
print(p2 <= p3)

# using the total_ordering decorator from standard library
@total_ordering
class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Point({self.x},{self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        return NotImplemented


p21, p22, p23, p24 = Point2(2, 3), Point2(
    4, 43), Point2(32, 33), Point2(32, 33)


print(p21 >= p24)
