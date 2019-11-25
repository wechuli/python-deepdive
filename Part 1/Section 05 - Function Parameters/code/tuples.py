# What defines a tuple in Python is not (), but ,

mytuple = 1, 2, 3, 4


print(type(mytuple))

# upacking

a, b, c = (12, 34, 'dfsd')
print(a, b, c)


empty_tuple = tuple()
print(empty_tuple)
