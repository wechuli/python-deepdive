import sys
from contextlib import contextmanager, redirect_stdout


@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file

    try:
        yield None
    finally:
        file.close()
        sys.stdout = current_stdout


with out_to_file('file.txt'):
    print('line 1')
    print('line 2')


print('line3')


# using inbuilt context manager to redirect stdout

with open('file2.txt', 'w') as f:
    with redirect_stdout(f):
        print('Steady is the way to go')
