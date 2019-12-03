import inspect


def simple_function():
    print('booo')


simple_function.custom = 'bohoo'


print(dir(simple_function))
print(dir(simple_function.__code__))


print(inspect.getmodule(print))
