a = 0

print(a)


def my_func():
    global a
    a = 100


my_func()
print(a)
