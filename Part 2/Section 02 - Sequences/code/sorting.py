items = ["hello", "python", "parrot", "bird"]


sorted_items = sorted(items, key=lambda element: element[-1])

print(sorted_items)

t = (10, 2, 3, 8, 9, 6, 1)

print(sorted(t))


s = {10, 3, 5, 8, 9, 6, 1}
d = {3: 100, 2: 200, 1: 10}
print(sorted(d))
print(sorted(d, key=lambda k: d[k]))

words = ("this", "is", "a", "late", "equalizer", "just")
print(sorted(words, key=lambda x: len(x)))

print(type(complex(10, 10)))
print(abs(complex(10, 10)))
