class Cities:

    def __init__(self):
        self._cities = ['Nairobi', 'Paris', 'Rome', 'London', 'Kampala']

    def __len__(self):
        return len(self._cities)

    class CityIterator:
        def __init__(self, city_obj):
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item

    def __iter__(self):
        return self.CityIterator(self)


for city in Cities():
    print(city)


for city in Cities():
    print(city)
