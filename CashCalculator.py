from Calculator import Calculator


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_cash_remained(self, currency):
        return self.records

