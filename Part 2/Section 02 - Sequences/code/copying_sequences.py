
from copy import deepcopy, copy

sequence = [10, 20, 30, 40, 50, ["shallow", "copy"]]

print(id(sequence[5]))
# shallow copy
sequence_shallow_copy = sequence.copy()
print(id(sequence_shallow_copy[5]))


# Deep copy
sequence_deep_copy = deepcopy(sequence)
print(sequence_deep_copy[5])
print(id(sequence_deep_copy[5]))


first = 1
sedond = 1

print(id(first), id(sedond))


mynumbers = [89.55, 1, 2, 3]
deep_numbers = deepcopy(mynumbers)

print(id(mynumbers[0]), id(deep_numbers[0]))
