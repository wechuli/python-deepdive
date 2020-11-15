from functools import reduce
from itertools import accumulate

my_list = [1, 2, 3, 4]

print(sum(my_list))

products = reduce(lambda x, y: x*y, my_list)
print(products)

# setting a different start value

sum_ = reduce(lambda x, y: x+y, my_list, 100)
print(sum_)


# accumulate

# unlike reduce, it returns intemerdiate values

prod_acc = accumulate(my_list, lambda x, y: x*y)


print(list(prod_acc))
