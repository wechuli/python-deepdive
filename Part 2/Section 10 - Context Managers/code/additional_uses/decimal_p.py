import decimal


class Precision:

    def __init__(self, precision: int) -> None:
        self._precision = precision
        self._current_prec = decimal.getcontext().prec

    def __enter__(self) -> None:
        decimal.getcontext().prec = self._precision

    def __exit__(self, exc_type, exc_value, exc_tb):
        decimal.getcontext().prec = self._current_prec
        return False


with Precision(3):
    print(decimal.getcontext().prec)


print(decimal.getcontext().prec)


# Inbuilt context manager in decimal class


with decimal.localcontext() as ctx:
    ctx.prec = 7
    print(decimal.getcontext().prec)

print(decimal.getcontext().prec)
