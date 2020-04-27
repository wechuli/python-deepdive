import random
from collections import namedtuple


l = [10, 20, 30, 40, 50]

print(random.choice(l))

weights = [3, 5, 3, 1, 4]

randoms = random.choices(l, k=3, weights=weights)

print(randoms)


Freq = namedtuple('Freq', ['count', 'freq'])


def freq_counter(lst):
    total = len(lst)
    return {k: Freq(lst.count(k), 100*lst.count(k)/total) for k in set(lst)}


print(freq_counter(random.choices(l, k=1_000_000, weights=weights)))
