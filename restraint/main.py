from restraint import io
from restraint.TimesPerUnit import TimesPerUnit

class Restraint:
    @classmethod
    def mark(cls, pipe, date):
        pipe.write(date + "\n")
        
    UNIT_CONVERSION = {
        "days":   TimesPerUnit.DAYS,
        "weeks":  TimesPerUnit.WEEKS,
        "months": TimesPerUnit.MONTHS,
        "years":  TimesPerUnit.YEARS,
        }

    @classmethod
    def test(cls, pipe, times, units, unit_string):
        marks = io.PlaintextPutter.read(pipe)
        
        # TODO check unit_string
        return TimesPerUnit(
            times,
            units,
            cls.UNIT_CONVERSION[unit_string]
          ).allows(marks)
