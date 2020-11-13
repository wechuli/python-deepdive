from datetime import date
from collections import namedtuple


file_name = "nyc_parking_tickets_extract.csv"


def generate_file_iterator(file_name: str):
    with open(file_name) as file:
        columns = next(file).strip('\n').split(',')
        new_columns = []

        for column in columns:
            new_columns.append(column.replace(" ", "_", -1).lower())

        Parking_data = namedtuple('Parking_data', new_columns)
        for row in file:
            yield Parking_data(*clean_datatypes(row))


def clean_datatypes(row: str) -> tuple:
    # split the data into a list
    row_list = row.strip('\n').split(',')
    if len(row_list) > 9:
        row_list = [*row_list[0:-2], row_list[-2] + row_list[-1]]

    return (int(row_list[0]), *row_list[1:4], parse_date_string(row_list[4]), int(row_list[5]), *row_list[6:])


def parse_date_string(date_string: str) -> date:
    date_split = date_string.split('/')
    return date(int(date_split[2]), int(date_split[0]), int(date_split[1]))


def calculate_violations_by_car_make(violations) -> dict:
    violations_by_make = {

    }

    for violation in violations:
        if violations_by_make.get(violation[7], None):
            violations_by_make[violation[7]] += 1
        else:
            violations_by_make[violation[7]] = 1
    return {k: v for k, v in sorted(violations_by_make.items(), key=lambda item: item[1], reverse=True)}


f = generate_file_iterator(file_name)
print(next(f))
print(calculate_violations_by_car_make(f))
