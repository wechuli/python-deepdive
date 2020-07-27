from collections import OrderedDict
names = ["Eric", "ffd"]
names = names + ["34", 5]

del names[0]

print(names)


suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']


alias = suits

print(id(alias), id(suits))


mylist = [1, 2, 3, 4, 5]
print(id(mylist))

mylist[0:2] = ('a', 'b', 'c', 'd')

print(mylist)
print(id(mylist))


mylist.extend({"hfd": 443, "dsd": 34, "dsd": "ds"})
print(mylist)


girls = ["Caroline", "Betty", "Jess", "June", "Liz", "Pauline"]

girls_short = girls[0:3]
print(id(girls), id(girls_short))
