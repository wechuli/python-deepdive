from itertools import compress

data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]

result = compress(data, selectors)

print(list(result))
