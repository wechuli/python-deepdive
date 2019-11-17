import cmath

i = 0 + 1j
euler_identity = cmath.exp(cmath.pi * i) + 1
print(euler_identity)


print(cmath.isclose(euler_identity, 0, abs_tol=0.0001))
