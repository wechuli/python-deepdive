
from copy import deepcopy, copy

sequence = [10, 20, 30, 40, 50, ["shallow", "copy"]]

print(id(sequence[5]))
# shallow copy
sequence_shallow_copy = sequence.copy()
print(id(sequence_shallow_copy[5]))


# Deep copy
sequence_deep_copy = deepcopy(sequence)
print(sequence_deep_copy[5])
print(id(sequence_deep_copy[5]))


first = 1
sedond = 1

print(id(first), id(sedond))


mynumbers = [89.55, 1, 2, 3]
deep_numbers = deepcopy(mynumbers)

print(id(mynumbers[0]), id(deep_numbers[0]))


# copying custom objects

class Point:
    def __init__(self, x: float, y: float) -> void:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Point({self.x},{self.y})'


class Line:
    def __init__(self, p1: Point, p2: Point) -> void:
        self.p1 = p1
        self.p2 = p2

    def __repr__(self) -> str:
        return f'Line({self.p1.__repr__()},{self.p2.__repr__()})'


p1 = Point(0, 0)
p2 = Point(10, 10)
line1 = Line(p1, p2)
line2 = deepcopy(line1)


