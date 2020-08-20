l = [1, 2, 3, 4, 5]


# A slice can be replaced with another iterable. For regular slices (not-extended), the slice and the iterable need not be the same length

print(l[1:3])

l[1:3] = (10, 20, 30, "er")

print(l)

# With extended slicing, the extended slice and the iterable must have the same length
l2 = [1, 2, 3, 4, 5, 6, 7]
l2[0:4:2] = 10, 30

print(l2)


# Deleting a Slice - Deletion is really just a special case of replacement. We simply assign an empty iterable - Works for standard slicing only

l3 = [1, 2, 3, 4, 5]
l3[1:3] = []
print(l3)


# Insertions using Slices - We can also insert elements using slice assignement

l4 = [1, 2, 3, 4, 5, 6]
# l4[1:1] = []
l4[1:1] = 'abcd'
print(l4)
