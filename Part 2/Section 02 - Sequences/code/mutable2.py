l = [1, 2, 3, 4, 5]
print(id(l))

l[0] = "of"

print(id(l))


def test_function(number: float, first_name: str, last_name: str) -> dict:
    return{
        "name": first_name + " " + last_name,
        "age": number.hex(),
        "done": True
    }


print(test_function(85.99, "Paul", "Wechuli"))


suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
l = [1, 2, 3, 4, 5]
l[0:2] = ('a', 'b', 'd', 'e')
print(l)
