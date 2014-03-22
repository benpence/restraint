import unittest
import datetime

import restraint

today      = datetime.datetime.today().date()
yesterday  = today - datetime.timedelta(days=1)
last_month = today - datetime.timedelta(days=31)
last_year  = today - datetime.timedelta(days=365)

tests = (
    {"add": (last_year, yesterday),
     "unmarked": (today, last_month),
     "after": (last_year, (yesterday,)),
     "ordering": (yesterday, last_year) },
    {"add": (today, today, last_month, yesterday),
     "unmarked": (last_year,),
     "after": (last_month, (yesterday, today)),
     "ordering": (today, yesterday, last_month) },
    )
    
class MarksTestCase(unittest.TestCase):
    def test_mark(self):
        for i, test in enumerate(tests):
            marks = restraint.Marks()

            for date in test["add"]:
                marks.mark(date)
            
            self.assertEqual(set(test["add"]), marks.dates)
        
    def test_is_marked(self):
        for test in tests:
            marks = restraint.Marks()

            for date in test["add"]:
                marks.mark(date)
            
            for date in test["add"]:
                self.assertTrue(marks.is_marked(date))
                
            for date in test["unmarked"]:
                self.assertFalse(marks.is_marked(date))

    def test_after(self):
        for test in tests:
            marks = restraint.Marks()

            for date in test["add"]:
                marks.mark(date)
                
            after, dates = test["after"]
            self.assertEqual(
                tuple(marks.after(after)),
                dates)

    def test_all(self):
        for test in tests:
            marks = restraint.Marks()

            for date in test["add"]:
                marks.mark(date)

            self.assertEqual(
                tuple(marks.all()),
                test["ordering"])
