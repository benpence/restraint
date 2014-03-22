from restraint import io
from restraint.TimesPerUnit import TimesPerUnit

class Restraint:
    @classmethod
    def mark(self, pipe, date):
        pipe.write(date + "\n")
        
    UNIT_CONVERSION = {
        "days":   TimesPerUnit.DAYS,
        "weeks":  TimesPerUnit.WEEKS,
        "months": TimesPerUnit.MONTHS,
        "years":  TimesPerUnit.YEARS,
        }

    @classmethod
    def test(self, pipe, times, units, unit_string):
        marks = io.PlaintextPutter.read(pipe)
        
        # TODO check unit_string
        return TimesPerUnit(
            times,
            units,
            self.UNIT_CONVERSION[unit_string]
          ).allows(marks)
