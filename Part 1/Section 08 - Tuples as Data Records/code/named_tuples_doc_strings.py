from collections import namedtuple


Point2D = namedtuple('Point2D', ('x', 'y'))


point1 = Point2D(12, 34)


print(point1)


for point in point1:
    print(point)


Vector2D = namedtuple('Vector2D', ('x1', 'y1', 'x2',
                                   'y2', 'origin_x', 'origin_y'))

vector_zero = Vector2D(0, 0, 0, 0, 0, 0)


v1 = vector_zero._replace(x1=10, y1=10, y2=20, x2=10)
print(v1)


def func(a, b=10, c=20):
    pass


print(func.__defaults__)
