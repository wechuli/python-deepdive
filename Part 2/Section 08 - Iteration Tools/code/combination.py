from itertools import combinations, product, islice
from collections import namedtuple
from fractions import Fraction

l1 = [1, 2, 3, 4]

comb = combinations(l1, 4)
print(list(comb))


SUITS = 'SHDC'
RANKS = tuple(map(str, range(2, 11))) + tuple('JQKA')

Card = namedtuple('Card', ['rank', 'suit'])
deck = (Card(rank, suit) for suit, rank in product(SUITS, RANKS))


sample_space = combinations(deck, 4)
total = 0
acceptable = 0

for outcome in sample_space:
    total += 1

    if all(map(lambda x: x.rank == 'A', outcome)):
        acceptable += 1

# for outcome in sample_space:
#     total += 1
#     for card in outcome:
#         if card.rank != 'A':
#             break
#     else:
#         acceptable += 1

print(f'total={total},acceptable={acceptable}')
print('odds={}'.format(Fraction(acceptable, total)))
print('odds = {:.10f}'.format(acceptable/total))
