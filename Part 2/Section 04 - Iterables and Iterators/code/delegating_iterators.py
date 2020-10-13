from collections import namedtuple

Person = namedtuple('Person', ['first', 'last'])


class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize(
            ) + ' ' + person.last.capitalize() for person in persons]

        except(TypeError, AttributeError):
            self._person = []

    def __iter__(self):
        return iter(self._persons)


persons = [Person('micheal', 'palin'), Person('jacky', 'groened'), Person(
    'paul', 'pogba'), Person('vivanee', 'midema')]

person_names = PersonNames(persons)

for p in person_names:
    print(p)
