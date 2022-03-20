from Calculator import Calculator
from datetime import datetime


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self):
        self.currency = int(self.limit) - sum(
            [int(self.records[i].amount)
             for i in range(0, int(len(self.records)))
             if self.records[i].date == datetime.now().date()])
        print(f'Осталось: {self.currency}')
        return self.currency

