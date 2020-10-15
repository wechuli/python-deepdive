import random


class Randoms:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            self.i += 1
            return random.randint(0, 100)


random.seed(0)
l = Randoms(10)


# if you pass an iterator to a function which iterates through the iterator, you will be unable to call elements of the iterator again

# e,g
print(min(l))

# the following is an error
print(max(l))


f = open('cars.csv')

for row in f:
    print(row, end='')
f.close()


def parse_data_row(row: str):
    row = row.strip('\n').split(';')
    return row[0], float(row[1])


def max_mpg(data):
    max_mpg = 0
    for row in data:
        _, mpg = parse_data_row(row)
        if mpg > max_mpg:
            max_mpg = mpg
    return max_mpg
