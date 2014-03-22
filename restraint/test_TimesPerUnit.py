import unittest
import datetime

import restraint
from restraint.TimesPerUnit import TimesPerUnit

today = datetime.datetime(2013, 8, 31).date()
days = (
    today,
    today - datetime.timedelta(days=2),
    today - datetime.timedelta(days=4),
    today - datetime.timedelta(days=7),
    today - datetime.timedelta(days=26),
    today - datetime.timedelta(days=27),
    today - datetime.timedelta(days=28),
    today - datetime.timedelta(days=363),
    today - datetime.timedelta(days=365),
    )

tests = (
    (False, 1,  3,  TimesPerUnit.DAYS),
    (False, 2,  3,  TimesPerUnit.DAYS),
    (False, 3,  5,  TimesPerUnit.DAYS),
    (True,  4,  5,  TimesPerUnit.DAYS),

    (False, 3,  1,  TimesPerUnit.WEEKS),
    (True,  5,  2,  TimesPerUnit.WEEKS),

    (False, 7,  1,  TimesPerUnit.MONTHS),
    (True,  8,  1,  TimesPerUnit.MONTHS),
    (False, 8,  12, TimesPerUnit.MONTHS),
    (True,  9,  12, TimesPerUnit.MONTHS),

    (False, 8,  1,  TimesPerUnit.YEARS),
    (True,  9,  1,  TimesPerUnit.YEARS),
    )

class TimesPerUnitTestCase(unittest.TestCase):
    def test_allows(self):
        for allows, times, units, unit in tests:
            marks = restraint.Marks(*days)
            restriction = TimesPerUnit(times, units, unit, today=today)

            self.assertEqual(
                allows,
                TimesPerUnit(times, units, unit, today=today).allows(marks))
