def dow_switch_fn(dow):
    if dow == 1:
        def fn(): return print('monday')
    elif dow == 2:
        def fn(): return print('tuesday')
    elif dow == 3:
        def fn(): return print('wednesday')
    else:
        def fn(): return print('Invalid day of weeek')

    return fn()


dow_switch_fn(3)
