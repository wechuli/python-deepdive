from parse_utils import csv_parser
from constants import fnames


# see a sample of what is in each file

for fname in fnames:
    print(fname)
    reader = csv_parser(fname, include_header=True)
    print(next(reader), end='\n')
