from Record import Record


class Calculator:
    def __init__(self, limit):
        if type(int(limit)) is int:
            self.limit = limit
            self.currency = limit
            self.records = []
        else:
            print('Not valid limit. Please try again')

    def add_record(self, record):
        if isinstance(record, Record):
            self.records.append(record)
        else:
            print('Input not valid')


    def get_today_stats(self, date):
        return self.records

    def get_week_stats(self):
        return self.records
