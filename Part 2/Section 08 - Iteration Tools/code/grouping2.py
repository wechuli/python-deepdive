from itertools import groupby


data = (1, 2, 2, 3)

grouped_data = groupby(data, lambda x: x)

for group_key, sub_iter in grouped_data:
    print(group_key, list(sub_iter))


data = (
    (1, 'abc'),
    (1, 'bcd'),
    (2, 'pyt'),
    (2, 'yth'),
    (2, 'tho'),
    (3, 'hon')
)

groups = groupby(data, lambda x: x[0])


for group_key, sub_iter in groups:
    print(group_key, list(sub_iter))


def gen_groups():
    for key in range(1, 4):
        for i in range(3):
            yield (key, i)


g = gen_groups()

groups = groupby(g, lambda x: x[0])

for group in groups:
    print(group[0], list(group[1]))
