from collections import namedtuple


Data = namedtuple('Data', ['name', 'age'])

d = Data(*['Paul', 27])

print(d.name)


print(d._fields)
