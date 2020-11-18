from itertools import groupby, islice


def get_length(iterable):
    length = 0
    for i in iterable:
        length += 1
    return length


with open('cars_2014.csv') as f:
    next(f)
    make_groups = groupby(f, lambda x: x.split(',')[0])
    make_counts = ((key, get_length(models)) for key, models in make_groups)
    print(list(make_counts))
