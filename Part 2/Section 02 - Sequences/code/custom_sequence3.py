class MyMutableSequence:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'MyMutableSequence(name={self.name})'

    def __add__(self, other) -> str:
        return MyMutableSequence(self.name + other.name)

    def __iadd__(self, other) -> str:
        if isinstance(other, MyMutableSequence):
            self.name += other.name
        else:
            self.name += other
        return self

    def __mul__(self, n: int):
        return MyMutableSequence(self.name * n)

    def __rmul__(self, n: int):

        return self.__mul__(n)

    def __imul__(self, n: int):
        self.name *= n
        return self

    def __contains__(self, value):
        return value in self.name


c1 = MyMutableSequence("Tricycle")
c2 = MyMutableSequence("Olympics")

print(f"ID of c1 = {id(c1)}, ID of c2 = {id(c2)} ")

result = c1 + c2
print(f'ID of result = {id(result)}')


c1 += c2
print(id(c1), c1)

result = c1 * 3
print(f'ID of result = {id(result)}')

c1 *= 3
print(id(c1), c1)
