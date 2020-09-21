s = {'x', 'y', 'b', 'c', 'a'}


for letter in s:
    print(letter)


class Squares:
    def __init__(self, length: int):
        self._length = length
        self._i = 0

    def __len__(self):
        return self._length

    def next_(self):
        if self._i >= self._length:
            raise StopIteration
        result = self._i ** 2
        self._i += 1
        return result


squares = Squares(4)

while True:
    try:
        print(squares.next_())
    except StopIteration:
        break
