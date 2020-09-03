
def decorator(message: str):
    def outer(fn):
        print(message)
        return fn
    return outer


@decorator("hi there")
def add(a: float, b: float) -> float:
    return a+b


test = add(23, 454)
print(test)
