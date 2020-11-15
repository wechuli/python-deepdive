from itertools import starmap
from operator import mul

# starmap

list_ = [[1, 2], [3, 4]]

mul_list = starmap(mul, list_)

for item in mul_list:
    print(item)
