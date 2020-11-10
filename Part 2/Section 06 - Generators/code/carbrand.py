file_1 = 'car-brands-1.txt'
file_2 = 'car-brands-2.txt'
file_3 = 'car-brands-3.txt'

files = file_1, file_2, file_3


def brands(*files):
    for f_name in files:
        with open(f_name) as f:
            for line in f:
                yield line.strip('\n')


def gen_clean_data(file):
    with open(file) as f:
        for row in f:
            yield row.strip('\n')


def brands_chain(*files):
    for f_name in files:
        yield from gen_clean_data(f_name)
