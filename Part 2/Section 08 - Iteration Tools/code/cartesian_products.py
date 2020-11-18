from itertools import product, tee


l1 = [1, 2, 3]
l2 = ['a', 'b', 'c', 'd']
l3 = [100, 200]

print(list(product(l1, l2, l3)))


def matrix(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f'{i} x {j} = {i*j}'


def matrix_product(n):
    result = ((i, j, i*j) for i, j in product(range(1, n+1), range(1, n+1)))
    yield from result


def matrix_product_tee(n):
    result = ((i, j, i*j) for i, j in product(*tee(range(1, n+1), 2)))
    yield from result


print(list(matrix_product_tee(5)))
