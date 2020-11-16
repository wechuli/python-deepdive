from itertools import zip_longest

numbers = [1, 2, 3, 4, 5]
names = ["June", "July", "August", "Sep"]
somet = ('a', 'b', 'c')


z = zip(numbers, names, somet)
print(list(z))

# zipping due to longest

z_longest = zip_longest(numbers, names, somet, fillvalue=None)
print(list(z_longest))


def integer(n):
    for i in range(n):
        yield i


def squares(n):
    for i in range(n):
        yield i ** 2


iter1 = integer(5)
inter2 = squares(6)

# print(list(iter1), list(inter2))

z_ex = zip(iter1, inter2)
print(list(z_ex))
print(list(iter1))
