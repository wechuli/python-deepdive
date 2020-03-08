from collections import namedtuple


class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


Point3D = namedtuple('Point3D', ('x', 'y', 'z'))


pt1 = Point3D(10, 20, 30)

print(pt1)
print(pt1[1])


pt2 = Point3D(x=45, y=90, z='ddf')
print(pt2)

print(pt1 is pt2)
print(pt1 == pt2)

print(pt1 == (10, 20, 30))


Circle = namedtuple('Circle', 'center_x center_y radius')
c = Circle(0, 0, 10)

print(c)


Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)
print(djia)
print(djia.close)


for item in djia:
    print(item)


symbol, year, *_, low, close = djia

print(symbol, year, low, close)
