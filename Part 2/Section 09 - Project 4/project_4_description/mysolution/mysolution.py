from itertools import groupby, islice
from collections import namedtuple
from csv import reader
from formatters import DataFormatter
from datetime import datetime, timedelta, timezone


personal_info = "personal_info.csv"
employment = "employment.csv"
vehicles = "vehicles.csv"
update_status = "update_status.csv"


def read_file(file_name):
    with open(file_name) as f:
        csv_reader = reader(f, delimiter=',', quotechar='"')
        yield from csv_reader


def create_formatted_data_iterator(file_iterator, formatter):
    for line in file_iterator:
        yield formatter(line)


def create_clean_data_iterator(file_name, formatter=DataFormatter.default_formatter):
    raw_file_iterator = read_file(file_name)
    # create named tuple to hold returned values
    Data = namedtuple('Data', next(raw_file_iterator))
    formarted_data_iterator = create_formatted_data_iterator(
        raw_file_iterator, formatter)
    for item in formarted_data_iterator:
        yield Data(*item)


def combined_iterator():
    personal_iterator = create_clean_data_iterator(personal_info)
    employment_iterator = create_clean_data_iterator(employment)
    vehicle_iterator = create_clean_data_iterator(
        vehicles, DataFormatter.vehicles_formatter)
    update_status_iterator = create_clean_data_iterator(
        update_status, DataFormatter.update_status_formatter)

    while True:

        try:
            p_data = next(personal_iterator)
            emp_data = next(employment_iterator)
            vehicle_data = next(vehicle_iterator)
            update_data = next(update_status_iterator)

            all_fields = p_data._fields + remove_ssn_field_from_tuple(emp_data._fields) + remove_ssn_field_from_tuple(
                vehicle_data._fields) + remove_ssn_field_from_tuple(update_data._fields)

            all_values = (*p_data, *remove_ssn_value_from_tuple(emp_data), *
                          remove_ssn_value_from_tuple(vehicle_data), *remove_ssn_value_from_tuple(update_data))

            Data = namedtuple('Data', all_fields)

            yield Data(*all_values)
        except StopIteration:
            break


def get_all_stale_records():
    combined_iter = combined_iterator()

    for item in combined_iter:
        cut_off = datetime(2017, 3, 1, tzinfo=timezone.utc)
        if item.last_updated < cut_off:
            continue
        yield item


def get_non_stale_records_by_gender():
    non_stale_records = get_all_stale_records()
    result_dict = {
        "Female": {

        },
        "Male": {

        },
        "total": 0
    }
    for record in non_stale_records:
        if record.gender == "Male":
            vehicle_make = record.vehicle_make
            if result_dict["Male"].get(vehicle_make, None):
                result_dict["Male"][vehicle_make] += 1
            else:
                result_dict["Male"][vehicle_make] = 1
        else:
            if result_dict["Female"].get(vehicle_make, None):
                result_dict["Female"][vehicle_make] += 1
            else:
                result_dict["Female"][vehicle_make] = 1
        result_dict["total"] += 1

    return result_dict


def remove_ssn_field_from_tuple(t: tuple) -> tuple:
    t_formatted = tuple(filter(lambda x: x != 'ssn', t))
    return t_formatted


def remove_ssn_value_from_tuple(t: tuple) -> tuple:
    named_tuple_value = t.ssn
    t_formatted = tuple(filter(lambda x: x != named_tuple_value, t))
    return t_formatted


print(get_non_stale_records_by_gender())
print(len(list(combined_iterator())))
