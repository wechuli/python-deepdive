from itertools import groupby, islice
from collections import defaultdict


makes = defaultdict(int)

with open('cars_2014.csv') as file:
    next(file)
    for row in file:
        make, _ = row.strip('\n').split(',')
        makes[make] += 1

print(makes)
