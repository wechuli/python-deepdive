def matrix(n: int):
    gen = ((i * j for j in range(1, n+1)) for i in range(n+1))
    return gen


def matrix_iterator(n):
    for row in matrix(n):
        for item in row:
            yield item


def matrix_iterator_yielf_from(n):
    for row in matrix(n):
        yield from row


m = list(matrix_iterator_yielf_from(5))
print(m)
