import inspect


def fake_function():
    print("This is a fake function")


print(inspect.getmodule(print))
print(inspect.getmodule(fake_function))
