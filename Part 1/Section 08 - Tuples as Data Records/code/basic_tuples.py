london = ("London", "UK", 8780000)


print(london[0])

print(type(london))


# unpacking

nairobi = ('Nairobi', 'Kenya', 85000)


city, country, population = nairobi
print(city, country, population)

city, _, population = ('Beijing', "China", 21000000000)
print(city, country, population)


record = ('DJIA', 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)

symbol, year, close = record[0], record[1], record[7]

# or

symbol, year, month, day, *_, close = record

print(_)


def print_tuple(tuple_sequence: tuple):
    for element in tuple_sequence:
        print(element)


print_tuple((1, 2, 3, 4, 5))


class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """returns representetion of the instance"""
        return f'{self.__class__.__name__}(x={self.x},y={self.y})'


pt = Point2D(10, 20)

print(pt)


a = Point2D(0, 0), Point2D(85, 89)
print(hex(id(a)))

print(a[0])

a[0].x = 89898989

print(a[0])

print(hex(id(a)))