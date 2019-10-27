## Types of numbers

- Integers (Z) - int
- Rational Numbers (Q) - fractions.Fraction
- Real Numbers (R) - float, decimal.Decimal
- Complex Numbers (C) - complex

Boolean truth values is alos considered as a type of numbers

### Integers

In Python, the **int** object uses a variable number of bits. Can use 4 byes (32 bits),8bytes (64bits),12 bytes. Seanless to us. Theoretically limited only by the amount of memory available. Larger numbers will use more memory and standard operators will run slower as numbers get larger

#### Integer Operations

+,-,\*,/,\*\*

- // is called floor division (div)
- % is called the modulo operator(mod)
  The floor of a real number a is the largest (in the standard number order) integer <= a

floor is not quite the same as truncation.

Be careful, a//b is not the integer portion of a/b, it is the floor of a/b
For a>0 and b>0, these are indeed the same thing

But beware when dealing with negative numbers

        a = b * (a//b) + a % b
