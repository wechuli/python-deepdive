my_list = ["cabbage", "lettuce", "zuchini", "cucumber", "banana"]

print(my_list.__getitem__(3))


class Silly:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        print('Called __len__')
        return self.n

    def __getitem__(self, value):
        print(type(value))
        if value < 0 or value >= self.n:
            raise IndexError
        return f' Element {value}'


silly = Silly(10)
# print(len(silly))
# for word in silly:
#     print(word)

print(silly[2])
print(silly[1:2])
