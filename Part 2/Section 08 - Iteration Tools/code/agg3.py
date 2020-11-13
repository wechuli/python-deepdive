
with open('car-brands.txt') as f:
    result = all(map(lambda row: len(row) >= 4, f))
print(result)


with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 10, f))

print(result)
