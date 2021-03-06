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

#### Fractional Numbers

Rational numbers are fractions of integer numbers.

Any real number with a finite number of digits after the decimal point is also a rational number.

Rational numbers can be represented in Python using the Fraction class in the fractions module. Fractions are automatically reduced. Negative sign, if any, is always attached to the numerator.

Fraction(numerator=0,denominator=1)
Fraction(other_fraction)
Fraction(float)
Fraction(decimal)
Fraction(string)

Standard arithmetic operators are supported and result in Fraction object as well

We can get the numerator and denominator of Fraction objects

float objects have finite precision => any float object can be written as a fraction.

Converting a float to a Fraction has an important caveat

Given a Fraction object, we can find an approximate equivalent fraction with a constrained denominator i.e finds the closest rational (which could be precisely equal) with a denominator that does not exceed max_denominator

## Floats

### Floats Internal Representations

The float class is Python's default implementation for representing real numbers. The Python (CPython) float is implemented using the C double type which(usually) implements the IEEE 754 double-precision binary float and also called binary64.
The float uses a fixed number of bytes -> 8bytes(64 bits)

The 64 bits are used up as follows

- **sign** -> 1 bit
- **exponent** -> 11 bits
- **significant digits** -> 52 bits -> 15-17 significant (base-10) digits

- Numbers can be represented as base-10 integers and fractions

The same problem that occurs when trying to represent 1/3 using a decimal expansion also happens when trying to represent certain numbers using a binary expansion. Some numbers that do have a finite decimal representation, do not have a finite binary representation and some do

### Coercing to Integers

data loss in all cases.

- truncation - simply returns the integer portion of the number, int constructor uses the trunc operation
- floor - the floor of a number is the largest integer less than (or equal to) the number - same as trunc for positive numbers but different when dealing with negative numbers
- ceiling - the ceiling of a number is the smallest integer greater than (or equal to) the number.
- rounding - python provides a built-in rounding function. This will round the number x to the closest mutliple of 10 -n

#### Banker's Rounding

- **IEEE 754 Standard** - rounds to the nearest value, with ties rounded to the nearest value with an even least significant digit. Banker's rounding is less biased rounding than ties away from zero.

### Decimals

alternative to using the (binary) float type -> avoids the approximation issues with floats finite number of significant digits. In Finance, banking and any other field where exact finite representations are highly desirable.

Decimals have a context that controls certain aspects of working with decimals:

- precision during arithmetic operations
- rounding algorithm

The context can be global -> the default context or temporary (local) -> sets temporary settings without affecting the global settings

ctx = decimal.getcontext() -> context(global in this case)
ctx.prec -> get or set the precision (value is an int)
ctx.rounding -> get or set the rounding mechanism (value is a string)

The **Decimal** class is in the decimal module
Decimal(x) x can be a variety of types -integers,other Decimal object,strings,tuples,floats(yes but not usually, pass as a string)

- Context precision affects mathematical operations
- Context precision does not affect the constructor

There are some drawbacks to the Decimal class vs the float class

- not as easy to code: construction via strings or tuples
- not all mathematical functions that exist in the math module have a Decimal counterpart
- more memory overhead
- performance: much slower than floats (relatively)

### Complex Numbers

Instantiated using the complex class.

- The standard arithmetic operators (+,-,/,\*,\*\*) work as expected with complex numbers. Real and complex numbers can be mixed
- The // and % are not supported
- The == and != operators are supported
- Comparison operators such as <,> <= >= are not supported
- Function in the math module will not work, use the cmath

### Booleans

Python has a concrete **bool** class that is used to represent Boolean values. However, the bool class is a subclass of the int class

is vs ==
Because True and False are singleton objects, they will always retain their same memory address throughout the lifetime of your application.

But since bool objects are also int objects, they can also be interpreted as the integers 1 and 0

All objects in Python have an associated truth value.

Every object has a True truth value except:

- None
- False
- )
- empty sequences (e.g list, tuple)
- empty mapping types (e.g dict,set)
- custom classes implementing \_

### Operator Precedence

- **()**
- **< > <= >= == != in is**
- **not**
- **and**
- **or**

### Boolean Operators and Truth Values

Normally, Boolean operators (NOT, OR, AND) are defined to operate on and return Boolean values. But every object in Python has a truth value (truthiness).
So, for any object X and Y, we could also write `bool(X)` and `bool(Y)` `bool(X)` or `bool(Y)`
In fact, we don't need to use `bool()` `X and Y` `X or Y`
So, what is returned when evaluating these expressions ?

#### Definition of or in Python

`X or Y` If X is truthy, returns X, otherwise returns Y or
If `X` is truthy, returns `X`, otherwise evaluates `Y` and returns it

#### Definition of and in Python

`X and Y` If `X` is falsy, returns `X`, otherwise returns `Y`
If X is falsy, returns `X`, otherwise evaluates `Y` and returns it

#### The Boolean not

**not** is a built-in function that returns a Boolean value

not `x` -> True if x is falsy
        -> False if x is truthy



## Comparison Operators
- binary operators
- evaluate to a **bool** value

- **Identity Operations** - `is` `is not` - compares memory address  - any type
- **Value Comparisons** - `==` `!=` compares values - different types OK, but must be compatible
- **Ordering Comparisons** - `<` `>` `<=` `>=` doesn't work for all types
- **Membership Operations** - `in` `not in` used with iterable types

### Numeric Types

Value comparisons will work with all numeric types
Mixed types (Except complex) in value and ordering