from datetime import datetime


class Period:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_diff_seconds(self):
        return (self.end - self.start).total_seconds()

    def get_diff_minutes(self):
        return (self.end - self.start).total_seconds() / 60

    def get_diff_hours(self):
        return (self.end - self.start).total_seconds() / 3600

    def get_diff_days(self):
        return (self.end - self.start).days


start = datetime(2023, 2, 1)
end = datetime(2023, 2, 5)

period = Period(start, end)

print(period.get_diff_seconds())
print(period.get_diff_minutes())
print(period.get_diff_hours())
print(period.get_diff_days())