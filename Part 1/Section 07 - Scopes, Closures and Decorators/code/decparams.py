from functools import wraps


def timed(n):

    def dec(fn):
        from time import perf_counter
        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(n):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)

            avg_run_time = total_elapsed / n
            print('Run time: {0:.6f}s'.format(avg_run_time))
            return result
        return inner
    return dec


def calc_fib_recusrive(n):
    return 1 if n < 3 else calc_fib_recusrive(n-2) + calc_fib_recusrive(n-1)


@timed(100)
def fib(n):
    return calc_fib_recusrive(n)


fib(20)
