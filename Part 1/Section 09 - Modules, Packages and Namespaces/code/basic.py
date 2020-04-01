import math
import fractions
import sys

print(math)
print(fractions)
print(globals())

PI: float = 3.142


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f'{self.name},{self.age}'

    def say_hello(self) -> tuple:
        return (self.name, self.age)


paul = Person()


def print_person(person: Person) -> str:
    person.say_hello()


def funct(number: float) -> float:
    p


print(sys.modules.get('math'))


lambda parameter_list: expression