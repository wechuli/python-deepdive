def do_nothing():
    print("I dont do anything")


print(hex(id(do_nothing)))
print(type(do_nothing))


a = 10
print(type(a))

b = int(85)
print(type(b))

c = int('101', base=2)
print(c)


def cube(a):
    return a ** 3


def returning_function():
    return cube


f = returning_function()
print(f(3))
