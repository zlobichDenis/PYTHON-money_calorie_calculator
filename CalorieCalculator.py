from Calculator import Calculator
from Record import Record


class CalorieCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_calories_remained(self):
        return self.records

