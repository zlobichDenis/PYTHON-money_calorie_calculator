from Record import Record
from CashCalculator import CashCalculator
from CalorieCalculator import CalorieCalculator

test_record = Record(amount=15, comment='test comment', date='20.03.2022')
cash_calculator = CashCalculator(input('Введите свой суточный лимит для трат: '))
calorie_calculator = CalorieCalculator(input('Введите свой суточный лимит для каллорий: '))

calorie_calculator.add_record(test_record)
cash_calculator.add_record(test_record)
cash_calculator.add_record(test_record)

cash_calculator.get_today_cash_remained()
calorie_calculator.get_calories_remained()
print(test_record.date)





