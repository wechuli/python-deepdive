def outer():
    x = 'Python'

    def inner():
        print(f"{x} rocks!")

    return inner


fn = outer()
fn()
