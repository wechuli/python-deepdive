class Squares:
    def __init__(self, n):
        self._n = n

    def __iter__(self):
        return Squares.squares(self._n)

    @staticmethod
    def squares(n: int):
        for i in range(n):
            yield i ** 2


sq = Squares(5)

# for i in sq:
#     print(i)

# for i in sq:
#     print(i)

print(list(sq))
print(list(sq))
