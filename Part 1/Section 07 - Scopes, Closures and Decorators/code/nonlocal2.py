

def outer_func():
    x = "hello"

    def inner_func():
        def inner_func2():
            nonlocal x
            x = 'python'
        inner_func2()
    inner_func()
    print(x)


outer_func()
