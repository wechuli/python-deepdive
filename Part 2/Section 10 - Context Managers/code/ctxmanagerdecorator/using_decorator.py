from typing import Generator, TextIO


class GenContextManager:
    def __init__(self, gen) -> None:
        self._gen = gen

    def __enter__(self) -> TextIO:
        print('calling next to get the yielded value from generator')
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('calling next to perform cleanup in generator')
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper


@context_manager_dec
def open_file(fname: str, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file..')
        f.close()


with open_file('test.txt') as f:
    print(f.readlines())
