from decimal import Decimal
my_tuple = (1, 2, 3, 866, "ee")


# input("Hi there")

for item in my_tuple:
    print(item)


print([1, 2, 3]+["dd", 'ds'])

x = [[0, 0]]
y = x + x
print(y)
y[0][0] = 100
print(y)
print(x)


t = ([1, 2, 3], 4, 5)


t[0].append(56)
print(t)

persons = {
    "a": 1, "b": 45
}
print(len(persons))

l = [100, 90, 20]
print("max", max(l), "min", min(l))


l = [10, 10.5, Decimal('20.3')]

print(min(l))


s = "enumreate something"

print(list(enumerate(s)))


girls = ["june", "jess", "caro", "her"]

print(list(enumerate(girls)))
print(list(zip(girls)))
