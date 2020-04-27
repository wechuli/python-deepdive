from time import perf_counter
import random

random.seed(0)


denoms = random.choices([0, 1], k=10_000_000, weights=[1, 9])

start = perf_counter()

for d in denoms:
    if d == 0:
        continue
    10/d

end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denoms):0.15f}')


start = perf_counter()

for d in denoms:
    try:
        10/d
    except ZeroDivisionError:
        continue


end = perf_counter()
print(f'Avg elapsed time: {(end-start)/len(denoms):0.15f}')
