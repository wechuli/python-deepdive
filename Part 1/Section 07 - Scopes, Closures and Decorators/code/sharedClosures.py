def pow(n):
    def inner(x):
        return x ** n
    return inner


square = pow(2)
print(square.__closure__)
cube = pow(3)
print(cube.__closure__)


def adder(n):
    def inner(x):
        return x + n
    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(2)

print(add_1.__closure__, add_2.__closure__, add_3.__closure__)


adders = []
# The code below is not a closure
for n in range(1, 4):
    adders.append(lambda x: x+n)


# to solve this, we use a function to form a closure
def create_adders():
    adders = []
    for n in range(1, 4):
        adders.append(lambda x: x+n)
    return adders
