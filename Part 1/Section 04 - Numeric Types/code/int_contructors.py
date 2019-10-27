a = int(10)
b = int(10.9)
c = int(True)
d = int("123")  # python automatically assumes the number is base10


print(c)
print(d)


# You can specify the base of the digits you pass to the int constructor. When used with a string, constructie has an optional second parameter: base 2<=base<=36. defaults to 10 when the base is not specified.

print(int('1010', base=2))


# base 16

print(int('A12F', base=16))

# base 8
print(int('534', base=8))

# converting back
print(bin(10))
print(oct(10))
print(hex(10))

# The prefixes in the strings help document the base of the number int('0xA',16) -> (10)10
# These prefixes are consisten with literal integers using a base prefix (no strings attached!)

a = 0b1010
a = 0o12
a = 0xfff

print(type(a))
print(a)
