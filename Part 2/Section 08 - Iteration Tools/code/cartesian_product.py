from itertools import product, tee, count, takewhile
from fractions import Fraction


def grid(min_val, max_val, step, *, num_dimensions=2):
    axis = takewhile(lambda x: x <= max_val, count(min_val, step))
    axes = tee(axis, num_dimensions)
    yield from product(*axes)


# print(list(grid(-1, 1, 0.5, num_dimensions=3)))


def all_possible_dices():
    dices = [i for i in range(1, 7)]
    dice_comb = product(*tee(dices, 2))
    yield from dice_comb


def determine_eight(comb):
    return sum(1 for i, j in comb if i+j == 8)


outcomes = list(filter(lambda x: x[0] + x[1] == 8, all_possible_dices()))

odds = Fraction(len(outcomes), len(list(all_possible_dices())))
print(odds)
