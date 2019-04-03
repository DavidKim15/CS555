import unittest
from datetime import datetime, timedelta

# Returns True if the date object date1 comes after today's date
# Returns False otherwise
def dateAfterCurrent(date1):
	today = datetime.today()
	if date1 > today:
		return True 
	return False

class TestDatesBeforeCurrentDate(unittest.TestCase):
	# Tests today's date
	def test_current_date(self):
		today = datetime.today()
		self.assertFalse(dateAfterCurrent(today))
	# Tests a date that is after the current date
	def test_after_current_date(self):
		today = datetime.today()
		thirtyDays = timedelta(days=30)
		thirtyDaysFromToday = today + thirtyDays
		self.assertTrue(dateAfterCurrent(thirtyDaysFromToday))
	# Tests a date that precedes current date
	def test_before_current_date(self):
		today = datetime.today()
		thirtyDays = timedelta(days=30)
		thirtyDaysBeforeToday = today - thirtyDays
		self.assertFalse(dateAfterCurrent(thirtyDaysBeforeToday))

if __name__ == '__main__':
	unittest.main()