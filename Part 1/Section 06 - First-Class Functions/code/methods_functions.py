class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def __repr__(self):
        return f'{self._first_name},{self._last_name}'


class Student(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


student = Student('Paul', 'Wechuli')
print(student)
