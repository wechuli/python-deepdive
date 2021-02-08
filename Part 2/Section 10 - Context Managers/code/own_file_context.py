class File:
    def __init__(self, name, mode) -> None:
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file...')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('closing file...')
        self.file.close()
        return False


with File('test.txt', 'w') as file:
    file.write("And you as well must die")
