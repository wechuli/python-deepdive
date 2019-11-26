a, *b = 1, 2, 3, 4, 5, 6
print(a)
print(b)

c, d, *e, f = 1, 2, 3, "dd", "yes", 56
print(c)
print(d)
print(e)
print(f)


l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [*l1, *l2]
print(l3)


d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}

d_final = [*d1, *d2, *d3]
print(d_final)
