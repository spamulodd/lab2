import datetime


class Date:

    def __init__(self, year, month, day):
        self.date = datetime.date(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_weekday(self):
        return self.date.weekday()

    def get_weekday_name(self):
        return self.date.strftime('%A')

    def get_month_name(self):
        return self.date.strftime('%B')


date = Date(2023, 2, 7)

print(date.get_year())
print(date.get_month())
print(date.get_day())
print(date.get_weekday())
print(date.get_weekday_name())
print(date.get_month_name())