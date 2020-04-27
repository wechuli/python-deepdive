from random import random, randint, shuffle, gauss
import random as rand
from collections import Counter


rand.seed(0)
for _ in range(10):

    print(randint(10, 20), random())


def generate_random_stuff(seed: int = None) -> list:
    rand.seed(seed)
    results = []

    for _ in range(5):
        results.append(randint(0, 5))

    characherts = list('abc')
    shuffle(characherts)
    results.append(characherts)

    for _ in range(5):
        results.append(gauss(0, 1))

    return results


# print(generate_random_stuff())
# print(generate_random_stuff(0))

def freq_analysis(lst: list) -> dict:
    return {k: lst.count(k) for k in set(lst)}


lst = [randint(0, 10) for _ in range(1_000_000)]

print(freq_analysis(lst))
