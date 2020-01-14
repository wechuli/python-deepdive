
def timed(reps):
    def dec(fn):
        from time import perf_counter
        from functools import wraps

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(10):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elasped = total_elapsed/10
            print(avg_elasped)
            return result
        return inner
    return dec


@timed(10)
def add(a, b):
    return a + b


print(add(34, 68))
