a = 100


def outer_func():
    b = 10

    def inner_func():
        print(a)
        print(b)
    inner_func()


outer_func()
