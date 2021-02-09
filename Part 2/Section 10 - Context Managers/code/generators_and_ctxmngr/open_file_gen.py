from typing import TextIO


class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs) -> None:
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


def open_file(fname, mode):
    f = open(fname, mode)
    try:
        print('opening file')
        yield f
    finally:
        print('closing file...')
        f.close()


with GenCtxManager(open_file, 'text.txt', 'w') as f:
    f.writelines('testing this \n and another line is here')

with GenCtxManager(open_file, 'text.txt', 'r') as f:
    print(f.readlines())
