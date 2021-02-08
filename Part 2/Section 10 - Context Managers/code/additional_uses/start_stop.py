from time import perf_counter, sleep


class Timer:
    def __init__(self) -> None:
        self._elapsed = 0

    def __enter__(self):
        self._start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._stop = perf_counter()
        self._elapsed = self._stop - self._start
        return False


with Timer() as timer:
    sleep(1)


print(timer._elapsed)
