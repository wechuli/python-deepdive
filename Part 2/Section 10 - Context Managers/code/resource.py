class Resource:
    def __init__(self, name: str) -> None:
        self.name = name
        self.state = None


class ResourceManager:
    def __init__(self, name) -> None:
        self.name = name
        self.resource = None

    def __enter__(self):
        print('entering context')
        self.resource = Resource(self.name)
        self.resource.state = 'created'
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exiting context')
        self.resource.state = 'destroyed'
        if exc_type:
            print('error occurred')
        return False


with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}')

print(f'{res.name} = {res.state}')
