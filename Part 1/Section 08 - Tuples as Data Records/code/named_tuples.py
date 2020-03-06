from collections import namedtuple


Point2D = namedtuple('Point2D', ['x', 'y'])

pt = Point2D(12, 34)
print(pt)


# we can't mutate the values

# pt.x = 30

print(Point2D._fields)
print(pt._asdict())
