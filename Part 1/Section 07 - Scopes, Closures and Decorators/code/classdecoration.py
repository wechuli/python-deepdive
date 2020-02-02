from fractions import Fraction

fraction = Fraction(2, 3)
# Monkey patching
Fraction.speak = lambda self, message: f'Fraction says {message}'

print(fraction.speak("This is a fun way to do stuff"))


fraction2 = Fraction(32, 44)
print(fraction2.speak("The parrot is no more"))


Fraction.is_integral = lambda self: self.denominator == 1


f1 = Fraction(2, 3)
f2 = Fraction(64, 8)

print(f1.is_integral())
print(f2.is_integral())

# decorating a class


def dec_speak(cls):
    cls.speak = lambda self, message: f'{self.__class__.__name__} says {message}'
    return cls
