from Record import Record
from datetime import datetime
from constants import date_format


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
        correct_format_date = datetime.strptime(date, date_format).date()
        today_stat = sum(
            [int(self.records[i].amount)
             for i in range(0, int(len(self.records)))
             if self.records[i].date == correct_format_date])
        return today_stat

    def get_week_stats(self):
        return self.records
