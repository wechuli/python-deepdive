class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number: float) -> float:
        self.total += number
        self.count += 1
        return self.total/self.count


averager = Averager()
print(averager.add(10))
print(averager.add(879))


def number_averager():
    total = 0
    count = 0

    def add(number: float):
        nonlocal total
        nonlocal count
        total += number
        count += 1
        return total/count
    return add


averager2 = number_averager()
print(averager2(10))
print(averager2(879))
