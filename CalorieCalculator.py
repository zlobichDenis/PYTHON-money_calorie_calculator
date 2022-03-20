from Calculator import Calculator
from Record import Record
from datetime import datetime


class CalorieCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        self.currency = int(self.limit) - sum(
            [int(self.records[i].amount)
             for i in range(0, int(len(self.records)))
             if self.records[i].date == datetime.now().date()])
        print(f'Осталось: {self.currency} ккал ')
        return self.currency

    def get_today_stats(self, date):
        today_stat = super().get_today_stats(date)
        print(f'Ваши траты на дату {date} составляют: {today_stat} ккал')

