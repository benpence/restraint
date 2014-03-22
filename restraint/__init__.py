class Marks:
    """Stores which days have been 'marked', or on which days an activity was performed"""

    def __init__(self, *dates):
        """dates is an iterable object that contains days already marked"""
        self.dates = set(dates)

    def mark(self, date):
        """Mark a day where the activity was performed"""
        self.dates.add(date)

    def is_marked(self, date):
        return date in self.dates
        
    def after(self, date):
        """Return a list, sorted earliest to latest, of marked days after 'date'"""
        return sorted(
            filter(
                lambda d: d > date,
                self.dates))

    def all(self):
        """Return a list, sorted latest to earliest, of marked days"""
        return sorted(
            (d for d in self.dates),
            reverse=True)

class Restriction:
    """Allow or restrict an activity based on which days it was performed in the past"""

    def allows(self, marks):
        """Based on when this activity was performed in the past (marks), can it be done today?"""
        return True
