number = 10.01


def addnumbers(additions):
    result = 0
    for i in range(additions):
        result += number
    return result


print(addnumbers(1000000000))
