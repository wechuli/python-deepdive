import dis

# list comprehension

l = [i**2 for i in range(5)]
g = (i**2 for i in range(5))


for item in g:
    print(item)


exp = compile('[i**2 for i in range(5)]', filename='<string>', mode='eval')
dis.dis(exp)

exp = compile('(i**2 for i in range(5))', filename='<string>', mode='eval')
dis.dis(exp)
