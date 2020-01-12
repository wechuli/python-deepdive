def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f"{run_dt}: called {fn.__name__}")
        return result

    return inner


def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        print(f"{fn.__name__} took {elapsed}s to run")

        return result

    return inner

# Stacked Decorators
@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))


print(fact(34))
