class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __repr__(self):
        return f'Rectangle: width={self._width}, height={self._height}'

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self._width == other._width) and (self._height == other._height)
        return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented

    def to_string(self):
        return f'Rectangle: width={self._width}, height={self._height}'

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2*(self._width + self._height)


r1 = Rectangle(12, 23)
r2 = Rectangle(12, 23)
r3 = Rectangle(20, 34)

print(r1 == r2)
print(r1 == 34)
print(r3 > r2)
