class Person:
  
    def __init__(self, name=None):
        self._name = name

    def __bool__(self):
        return bool(self._name)


person1 = Person()
person2 = Person(name="Wechuli")


print(bool(person1))
print(bool(person2))
