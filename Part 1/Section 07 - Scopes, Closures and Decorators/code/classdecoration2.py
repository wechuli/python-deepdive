from datetime import datetime, timezone
from math import sqrt


def info(self):
    results = []
    results.append(f'time:{datetime.now(timezone.utc)}')
    results.append('Class: {self.__class__.__name__}')
    results.append(f'id:{hex(id(self))}')
    for k, v in vars(self).items():
        results.append(f'{k}:{v}')
    return results


def debug_info(cls):

    cls.debug = info
    # returning the class is not necessary, since we are mutating the class but it is necessary if we are going to use the short decorator syntax @
    return cls

# decorating classes


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return 'Hello there'


paul = Person('Paul', 1939)

print(paul.debug())


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed')
        else:
            self._speed = new_speed


favorite = Automobile('Ford', 'Model T', 1908, 45)
print(favorite.debug())
favorite.speed = 40
print(favorite.debug())


