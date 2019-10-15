for i in range(5):
    print(i)

for word in ['hello', "world", "you"]:
    print(word)

for i in range(5):
    if i == 3:
        continue
    print(i)


for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiples of 7 in the range')
