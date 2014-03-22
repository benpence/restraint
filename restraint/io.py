import datetime

import restraint
import io

class Reader:
    """Creates a restraint.Marks object from a readable file object"""
    def read(self, pipe):
        return restraint.Marks()
        
class Writer:
    """Creates a readable file object from a restraint.Marks object for starage on disk"""
    def write(self, pipe):
        return io.StringIO("")

class PlaintextPutter(Reader, Writer):
    """Uses a plaintext format for constructing and storing restraint.Marks objects.
Each line must be of the format YYYY/MM/DD to be recognized as a date."""
    DATE_FORMAT = "%Y/%m/%d"

    @classmethod
    def read(cls, pipe):
        dates = set()
        
        for line in pipe.readlines():
            try:
                date = datetime.datetime.strptime(
                    line.strip(),
                    cls.DATE_FORMAT).date()
                dates.add(date)

            # Invalid lines are ignored
            except:
                continue
        return restraint.Marks(*dates)

    @classmethod
    def write(cls, marks):
        lines = "\n".join(
            # Convert dates to YYYY/MM/DD
            map(lambda d: d.strftime(
                    cls.DATE_FORMAT),
                marks.all()))
        
        return io.StringIO(lines)
