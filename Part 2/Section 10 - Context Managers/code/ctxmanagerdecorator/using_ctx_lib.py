from contextlib import contextmanager


@contextmanager
def open_file(fname: str, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file..')
        f.close()


with open_file('test.txt', 'r') as f:
    print(f.readlines())
