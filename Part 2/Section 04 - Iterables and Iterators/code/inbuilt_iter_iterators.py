# range is an iterable

r = range(10)

for i in r:
    print(i)

# zip is an iterator

z = zip(['a', 'b', 'c'], [1, 2, 3])
print(list(z))

print('__next__' in dir(z))

# open

with open('../cars.csv') as f:
    print(type(f))
    l = f.readlines()
    print('__iter__' in dir(f))
    print('__next__' in dir(f))
    print(l[0:12])

origins = set()
with open('cars.csv') as f:
    rows = f.readlines()

for row in rows[2:]:
    origin = row.strip('\n').split(';')[-1]
    origins.add(origin)

# enumerator

e = enumerate('Python Rocks!')
print(list(e))


# dicts

person = {
    "name": "Paul",
    "age": 27,
    "hobbies": ["football", "programming"]
}

print(person.keys())
