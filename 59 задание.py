import calendar

class Month:

  def __init__(self, number):
    self.number = number

  def get_number(self):
    return self.number

  def get_name(self):
    return calendar.month_name[self.number]

  def get_last_day(self):
    return calendar.monthrange(2023, self.number)[1]

  def get_first_weekday(self):
    return calendar.monthrange(2023, self.number)[0]

  def get_last_weekday(self):
    return calendar.monthrange(2023, self.number + 1)[0]

jan = Month(1)

print(jan.get_number()) # 1
print(jan.get_name()) # January
print(jan.get_last_day()) # 31
print(jan.get_first_weekday()) # 5
print(jan.get_last_weekday()) # 1