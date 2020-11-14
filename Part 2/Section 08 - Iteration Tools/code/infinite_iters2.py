from collections import namedtuple
from itertools import cycle, repeat


Card = namedtuple('Card', ['rank', 'suit'])


def card_deck():
    ranks = tuple(str(num) for num in range(2, 11)) + tuple('JQKA')
    suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    for suit in suits:
        for rank in ranks:
            yield Card(rank, suit)


hands = [list() for _ in range(4)]
index = 0

for card in card_deck():
    index = index % 4
    hands[index].append(card)
    index += 1


hands = [list() for _ in range(4)]
index_cycle = cycle([0, 1, 2, 3])
for card in card_deck():
    hands[next(index_cycle)].append(card)


# repeat

g = repeat('Python')


for i in range(5):
    print(next(g))


print(list(repeat('.NET 5', 10)))
