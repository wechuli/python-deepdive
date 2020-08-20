# in place concat

l1 = [1, 2, 3]
l2 = [4, 5, 6]


print(hex(id(l1)))

l1 += l2
print(l1)


print(hex(id(l1)))


# in place repetation

l3 = [1, 2, 3]
print(hex(id(l3)))
l3 *= 3

print(hex(id(l3)))
