from collections import namedtuple


Card = namedtuple('Card', ['rank', 'suit'])
SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')


def card_generator():
    for i in range(len(SUITS) * len(RANKS)):
        suit = SUITS[i // len(RANKS)]
        rank = RANKS[i % len(RANKS)]
        card = Card(rank, suit)
        yield card


for card in card_generator():
    print(card)


# iterator- lazy evaluation
def card_gen2():
    for suit in SUITS:
        for rank in RANKS:
            yield Card(rank, suit)


class CardDeck:
    Card = namedtuple('Card', ['rank', 'suit'])
    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    RANKS = tuple(range(2, 11)) + tuple('JQKA')

    def __init__(self):
        pass

    def __iter__(self):
        return CardDeck.card_gen()

    def __reversed__(self):
        return CardDeck.reversed_card_gen()

    @staticmethod
    def card_gen():
        for suit in CardDeck.SUITS:
            for rank in CardDeck.RANKS:
                yield Card(rank, suit)

    @staticmethod
    def reversed_card_gen():
        for suit in reversed(CardDeck.SUITS):
            for rank in reversed(CardDeck.RANKS):
                yield Card(rank, suit)
