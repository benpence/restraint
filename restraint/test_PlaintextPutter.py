import unittest
import datetime
import io

import restraint
from restraint import io as rio


tests = (
    ("2014/01/01\n" +
     "2014/01/02\n" +
     "2013/01/02\n",
     "2014/01/02\n" +
     "2014/01/01\n" +
     "2013/01/02",
     (datetime.datetime(2014, 1, 2).date(),
      datetime.datetime(2013, 1, 2).date(),
      datetime.datetime(2014, 1, 1).date())),
    ("hello\n" +
     "2013/05/06\n" +
     "there you are\n",
     "2013/05/06",
     (datetime.datetime(2013, 5, 6).date(),)),
)

class PlaintextPutterTestCase(unittest.TestCase):
    def test_read(self):
        for s, clean_s, dates in tests:
            pipe = io.StringIO(s)
            
            self.assertEqual(
                rio.PlaintextPutter.read(pipe).dates,
                set(dates))

    def test_write(self):
        for s, clean_s, dates in tests:
            result = rio.PlaintextPutter.write(
                restraint.Marks(*dates))

            self.assertEqual(
                result.read(),
                clean_s)
