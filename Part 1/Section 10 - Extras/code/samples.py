import random

l = list(range(10))

print(random.choices(l, k=5))
print(random.sample(l, k=6))


suits = ('C', 'D', 'H', 'S')
ranks = tuple(range(2, 11)) + tuple('JQKA')


deck = [str(rank) + suit for suit in suits for rank in ranks]
print(suits, ranks, deck)

print(random.sample(deck, k=10))
