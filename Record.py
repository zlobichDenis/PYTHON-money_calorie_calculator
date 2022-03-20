import datetime as dt
from constants import date_format


class Record:
  def __init__(self, amount, comment, date):
    self.amount = amount
    self.comment = comment
    self.date = dt.datetime.strptime(date, date_format).date()
