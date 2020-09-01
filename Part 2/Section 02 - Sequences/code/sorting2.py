class MyClass:
    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __repr__(self):
        return f'MyClass({self.name},{self.val})'

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val
