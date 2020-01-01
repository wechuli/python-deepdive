from operator import attrgetter, itemgetter


comp_list = [5-10j, 3+3j, 2-100j, 45+90j]


print(sorted(comp_list, key=lambda x: x.real))


# using opertaor module
print(sorted(comp_list, key=attrgetter('real')))

list_of_tuples = [(2, 3, 4), (1, 3, 5), (6,), (4, 100)]
print(sorted(list_of_tuples, key=itemgetter(0)))
