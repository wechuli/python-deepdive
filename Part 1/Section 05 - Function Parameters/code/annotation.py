def my_func(a: str, b: str) -> str:
    return a * b


help(my_func)

my_func()

# with default values


def my_func_args(a: str = 'xyz', b: int = 1) -> str:
    pass
