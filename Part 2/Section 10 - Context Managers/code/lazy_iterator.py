import csv


def read_data():
    with open('nyc_parking_tickets_extract.csv') as f:
        yield from csv.reader(f, delimiter=',', quotechar='"')


reader = read_data()

print(type(reader))

print(next(reader))
