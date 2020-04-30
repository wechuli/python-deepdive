_sentinel = object()


def validate(a=_sentinel):
    default_a = validate.__defaults__[0]
    if a is not default_a:
        print('argument was provided')
    else:
        print('argument was NOT provided')


validate()
validate(None)


def validate_two(a=object(), b=object(), *, kw=object()):

    default_a = validate_two.__defaults__[0]
    default_b = validate_two.__defaults__[1]
    default_kw = validate_two.__kwdefaults__['kw']
    print(default_a, default_b, default_kw)


validate_two()
validate_two(23, 43, kw=3)
