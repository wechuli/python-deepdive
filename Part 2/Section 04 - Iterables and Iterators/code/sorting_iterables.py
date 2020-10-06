import random


random.seed(0)
randint = random.randint


class RandomInts:
    def __init__(self, length, *, seed=0, lower=0, upper=10):
        self._length = length
        self._seed = seed
        self._lower = lower
        self._upper = upper

    def __len__(self):
        return self._length

    def __iter__(self):
        return self.RandomIterator(self._length, seed=self._seed, lower=self._lower, upper=self._upper)

    class RandomIterator:
        def __init__(self, length, *, seed, lower, upper):
            self._length = length
            self._seed = seed
            self._lower = lower
            self._upper = upper
            self._num_requested = 0
            random.seed(seed)

        def __iter__(self):
            return self

        def __next__(self):
            if self._num_requested >= self._length:
                raise StopIteration
            else:
                result = randint(self._lower, self._upper)
                self._num_requested += 1
                return result


randoms = RandomInts(10)

print(sorted(randoms, reverse=True))
