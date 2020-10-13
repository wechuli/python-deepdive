from collections import namedtuple


class Deck:
    # class attributes
    _suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    _ranks = tuple(range(2, 11)) + tuple('JQKA')
    Card = namedtuple('Card', ['rank', 'suit'])

    def __init__(self):
        self.length = len(Deck._suits) * len(Deck._ranks)

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.CardDeckIterator(self.length)

    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse=True)

    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length = length
            self.reverse = reverse
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1 - self.i
                else:
                    index = self.i
                suit = Deck._suits[self.i//len(Deck._ranks)]
                rank = Deck._ranks[self.i % len(Deck._ranks)]
                self.i += 1
                return Deck.Card(rank, suit)


deck = Deck()

for card in deck:
    print(card)
