from collections import namedtuple


City = namedtuple('City', ['size', 'population', 'country'])


nairobi = City(country="KE", size=50_000, population=3_000_000)
dar_esalam = City(20_000, 2_000_000, "TZ")


for prop in nairobi:
    print(prop)


