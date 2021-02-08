import sys


class OutToFile:
    def __init__(self, fname) -> None:
        self._fname = fname
        self._current_stdout = sys.stdout

    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file

    def __exit__(self, exc_type, exc_value, exc_tb):
        sys.stdout = self._current_stdout
        self._file.close()
        return False


with OutToFile('test.txt'):
    print("And you as well must die beloved dust")
    print("And all your beauty stand you in no stead")
