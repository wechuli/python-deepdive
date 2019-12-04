

def my_func(a: "mandatory positional",
            b: "optional positional" = 1,
            c=2,
            *args: "adds extra positional here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "provides extra kw-only here") -> "does nothing":
    """
    This function does nothing but does have various parameters and annotations
    """
    i = 10
    j = 20
