def outer():
    a = 100
    x = 'python'
    y = 'programming'

    print(hex(id(x)))
    print(hex(id(y)))

    def inner():
        a = 10  # local variables
        print(f"{x} rocks")
        print(y)

    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)


def counter():
    count = 0
    fakelist = []

    def inc():
        nonlocal count
        nonlocal fakelist

        count += 1000
        fakelist.append(78)
        return count
    return inc


print("........................")

fn = counter()
print(fn.__closure__)
fn()
print(fn.__closure__)


print("........................")

fn2 = counter()
print(fn2.__closure__)
fn2()
print(fn2.__closure__)
