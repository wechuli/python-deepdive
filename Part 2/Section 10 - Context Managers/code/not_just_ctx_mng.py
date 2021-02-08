from io import TextIOWrapper


class DataIterator:
    def __init__(self, fname) -> None:
        self._fname = fname
        self._f: TextIOWrapper = None

    def __iter__(self):
        return self

    def __next__(self):
        row: str = next(self._f)
        return row.strip('\n').split(',')

    def __enter__(self):
        self._f = open(self._fname)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if not self._f.closed:
            self._f.close()
        return False


with DataIterator('nyc_parking_tickets_extract.csv') as data:
    for row in data:
        print(row)
