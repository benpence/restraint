import datetime
import math

import restraint

class TimesPerUnit(restraint.Restriction):
    TODAY = datetime.datetime.today().date()

    def DAYS(self, quantity):
       return self.today - datetime.timedelta(days=quantity)

    def WEEKS(self, quantity):
        return self.DAYS(quantity * 7)

    MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # BUG is not leap year aware. months are stupid anyway
    def MONTHS(self, quantity):
        years_back = int(math.ceil(
            float(quantity - (self.today.month - 1)) / 12))

        month = ((self.today.month - 1 - quantity) % 12) + 1

        if self.MONTH_DAYS[month - 1] < self.today.day:
            days = TimesPerUnit.MONTH_DAYS[month - 1]
        else:
            days = self.today.day

        return datetime.date(
            self.today.year - years_back,
            month,
            days)

    def YEARS(self, quantity):
        return self.DAYS(quantity * 365)

    def __init__(self, times, units, unit, today=TODAY):
        self.times = times
        self.units = units
        self.unit = unit
        self.today = today

    def allows(self, marks):
        times_since = len(
            marks.after(
                self.unit(self, self.units)))

        return times_since < self.times
