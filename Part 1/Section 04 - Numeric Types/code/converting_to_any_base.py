# Write a program that takes a number in base 10 and converts it no another base
MAPPING_ENCODING = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def from_base10(n: int, b: int):
    if b < 2:
        raise ValueError('Base b must be >=2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # m, n = n % b, n//b
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits


def encode(digits: list, digit_map: str):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not long enough to encode the digits')
    # encoding = ''
    # for d in digits:
    #     encoding += digit_map[d]
    # return encoding
    return ''.join([digit_map[d] for d in digits])


def rebase_from10(number: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    sign = -1 if number < 0 else 1
    number *= sign
    digits = from_base10(number, base)
    encoding = encode(digits, MAPPING_ENCODING)
    if sign == -1:
        encoding = '-' + encoding
    return encoding


e = rebase_from10(10, 2)
print(e)
print(int(e, base=2))

e = rebase_from10(3451, 16)
print(e)
print(int(e, base=16))


e = rebase_from10(-1055, 2)
print(e)
print(int(e, base=2))