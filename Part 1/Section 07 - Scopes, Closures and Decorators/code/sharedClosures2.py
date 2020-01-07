def outer():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count
    return inc1, inc2


inc1, inc2 = outer()


print("Inc 1 introspection before")
print(inc1.__code__.co_freevars)
print(inc1.__closure__)
print(inc1())
print("Inc 1 introspection after")
print(inc1.__code__.co_freevars)
print(inc1.__closure__)


print("Inc 2 introspection before")
print(inc2.__code__.co_freevars)
print(inc2.__closure__)
print(inc2())
print("Inc 2 introspection after")
print(inc2.__code__.co_freevars)
print(inc2.__closure__)
