from itertools import tee

squares = (i**2 for i in range(1, 20))

# make copies of the generator
iters = tee(squares, 3)

print(iters)

# tee function returns a tuple of generatos

iter1, iter2, iter3 = iters

print(next(iter1))
print(next(iter2))
print(next(iter3))


# we can tee lists, also returns an itertor copies

l = [1, 2, 3, 4]

list_iter = tee(l, 3)


print(list_iter)
print(dir(list_iter[0]))
print(list_iter[0][0])
