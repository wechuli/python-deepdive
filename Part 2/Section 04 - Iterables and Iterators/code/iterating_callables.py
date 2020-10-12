def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i
    return inc


class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self.counter_callable = counter_callable
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration

        result = self.counter_callable()
        if result == self.sentinel:
            self.is_consumed = True
            raise StopIteration
        else:
            return result


cnt = counter()
cnt_iter = CounterIterator(cnt, 5)

for c in cnt_iter:
    print(c)

print(cnt_iter.__next__())
