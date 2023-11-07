from datetime import datetime, timedelta


class Date:

    def __init__(self, year, month, day):
        self.date = datetime(year, month, day)

    # остальные методы класса Date


class DateExt(Date):

    def add_years(self, years):
        return Date(self.date.year + years, self.date.month, self.date.day)

    def subtract_years(self, years):
        return Date(self.date.year - years, self.date.month, self.date.day)

    def add_months(self, months):
        return Date(self.date.year, self.date.month + months, self.date.day)

    def subtract_months(self, months):
        return Date(self.date.year, self.date.month - months, self.date.day)

    def add_days(self, days):
        return Date(self.date + timedelta(days=days))

    def subtract_days(self, days):
        return Date(self.date - timedelta(days=days))


date = DateExt(2020, 2, 20)
new_date = date.add_years(2)

print(new_date.get_year())  # 2022