import time


def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end-start) / rep


def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n ** i)
    return results


def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    # using generators
    return (n**i for i in range(start, end))


print(time_it(compute_powers_1, 2, start=0, end=20000, rep=5))
print(time_it(compute_powers_2, 2, start=0, end=20000, rep=5))
print(time_it(compute_powers_3, 2, start=0, end=20000, rep=5))
