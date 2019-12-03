l = ['a', 'B', 'c', 'D']

print(sorted(l))

print(sorted(l, key=lambda letter: letter.upper()))


mydict = {
    "def": 300,
    "abc": 200,
    "ghi": 100,
    "xyz": 85,
    "fdd": 986
}


print(sorted(mydict, key=lambda dict_key: mydict[dict_key]))


def dist_sq(x):
    return (x.real)**2 + (x.imag)**2


complex_numbers = [3+3j, 1-1j, 0, 3+0j, 2-56j]

print(sorted(complex_numbers, key=dist_sq))

my_list = ['Clease', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
my_list = ['Idle', 'Clease', 'Palin', 'Chapman', 'Gilliam', 'Jones']

print(sorted(my_list, key=lambda s: s[-1]))
