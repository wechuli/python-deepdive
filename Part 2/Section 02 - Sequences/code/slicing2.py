
s = slice(0, 3)

items = ["unga", "beans", "chicken", "cabbage", "kales", "eggs"]

items_slice = items[s]

print(items_slice)
print(items_slice[0:100])


# getting equivalent ranges

new_slice = slice(9, -90, -3)

equivalent_range = new_slice.indices(6)
print(equivalent_range)


l = 'python'

print(l[::-1])
print(l[len(l):-10:-1])
print(l[5:-len(l)-1:-1])
