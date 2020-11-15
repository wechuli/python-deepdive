from itertools import chain

l1 = [i**2 for i in range(4)]
l2 = [i**2 for i in range(4, 8)]
l3 = [i**2 for i in range(8, 12)]

# using chain
l_chained = chain(l1, l2, l3)

for item in l_chained:
    print(item)


# chain from iterables

l_iter_chained = chain.from_iterable((l1, l2, l3))

for item in l_iter_chained:
    print(item)
