class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("Width must be a positive number")
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive')
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

    def get_width(self):
        return self._width

    def to_string(self):
        return f'Rectangle: width={self._width}, height={self._height}'

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2*(self._width + self._height)


r1 = Rectangle(10, 20)
print(r1.get_width())
print(r1.height)
r1.height = 90
print(r1.height)

# r2 = Rectangle(-10, 20)