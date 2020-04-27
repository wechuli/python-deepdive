print('{} % {}'.format(10, 3, 10 % 3))
print('{1} % {2} = {0}'.format(10 % 3, 10, 3))


print(f'10 % 3 = {10 % 3}')


def outer():
    name = 'Python'

    def inner():
        return f'{name} rocks'

    return inner


print(outer()())


sq = lambda x: x**2
a = 10
b=1