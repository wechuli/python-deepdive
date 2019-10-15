class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __repr__(self):
        return f'Rectangle: width={self._width}, height={self._height}'

    def to_string(self):
        return f'Rectangle: width={self._width}, height={self._height}'

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2*(self._width + self._height)


r1 = Rectangle(10, 20)

print(r1.area())
print(r1.perimeter())
print(r1)
print(dir(Rectangle))
print(str(r1))
