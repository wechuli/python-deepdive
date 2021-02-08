from datetime import datetime

class DataFormatter:
    def __init__(self):
        pass

    @staticmethod
    def default_formatter(line):
        """
        This formatter does nothing
        """
        return tuple(line)

    @staticmethod
    def vehicles_formatter(line):
        """
        formatter should change last value from string to integer
        """
        return tuple(line[0:-1]) + tuple([int(line[-1])])

    @staticmethod
    def update_status_formatter(line):
        """
        formatter converts last two values in the list to dates
        """
        date_format = "%Y-%m-%dT%H:%M:%S%z"
        updated = datetime.strptime(line[1], date_format)
        created = datetime.strptime(line[2], date_format)
        return (line[0], updated, created)
