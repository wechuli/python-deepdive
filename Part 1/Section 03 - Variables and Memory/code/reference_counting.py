import sys
import ctypes


my_var = 10
other_var = my_var

print(hex(id(my_var)))
print(hex(id(other_var)))
print(sys.getrefcount(my_var))


a = [1, 2, 3]
print(sys.getrefcount(a))


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(a)))
b = a
print(ref_count(id(a)))
c = b
print(ref_count(id(a)))
c = 10
print(ref_count(id(a)))


a_id = id(a)
a = None
print(ref_count(a_id))
