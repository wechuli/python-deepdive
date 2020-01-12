def dec_1(fn):
    def inner(*args, **kwargs):
        print(f"Running dec_1, the function to be decorated: {fn.__name__}")
        return fn(*args, **kwargs)
    return inner


def dec_2(fn):
    def inner(*args, **kwargs):
        print(f"Running dec_2, the function to be decorated: {fn.__name__}")
        return fn(*args, **kwargs)
    return inner


@dec_1
@dec_2
def my_func(a, b):
    print("Runnign my_func")
    return a * b


my_func(12, 44)
