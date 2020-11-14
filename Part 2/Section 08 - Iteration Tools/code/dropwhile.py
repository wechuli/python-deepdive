from itertools import takewhile, dropwhile
from math import sin, pi


def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start)/(n-1)
    for _ in range(n):
        yield round(sin(start), 2)
        start += step


# print(list(sine_wave(15)))

# takewhile

result = takewhile(lambda x: 0 <= x <= 0.9, sine_wave(15))
# result = takewhile(lambda x: x >= 0 and x <= 0.9, sine_wave(15))
print(list(result))


print(0 <= 6 <= 10)


# drop while

l = [1, 3, 5, 2, 1]


result = dropwhile(lambda x: x < 5, l)
print(tuple(result))
