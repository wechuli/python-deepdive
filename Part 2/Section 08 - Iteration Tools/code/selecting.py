from itertools import filterfalse

my_list = [1, 2, 3, 4, 5, 300, -4, 3, 7]


result = filter(lambda x: x > 5, my_list)

print(list(result))


def gen_cubes(n):
    for i in range(n):
        yield i ** 3


odd_cubes = filter(lambda x: x % 2 == 1, gen_cubes(20))

print(list(odd_cubes))

# using filterfalse
even_cubes = filterfalse(lambda x: x % 2 == 1, gen_cubes(20))
print(list(even_cubes))
