from random import uniform
from math import sqrt

london = 'London', 'UK', 8_780_000
nairobi = 'Nairobi', 'Kenya', 4_397_073
beijing = 'Beijing', 'China', 21_000_000


print(london)


cities = [london, nairobi, beijing]
print(cities)

print(sum(city[2] for city in cities))


record = ('DJIA', 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)


symbol, *_, close = record


print(symbol)
print(close)


for city, country, population in cities:
    print(city, country, population)

for item in enumerate(cities):
    print(item)


def random_shot(radius):
    random_x = uniform(-radius, radius)
    random_y = uniform(-radius, radius)

    if sqrt(random_x ** 2 + random_y ** 2) <= radius:
        is_in_circle = True
    else:
        is_in_circle = False

    return random_x, random_y, is_in_circle


num_of_attempts = 100
count_inside = 0

for i in range(num_of_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1

