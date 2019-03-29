import unittest
from datetime import datetime, timedelta
# If you want to run this locally, remove "jordan."
from jordan.us03birthBeforeDeath import getDate

# Returns True if the person record has been born in the past 30 days, returns 
# False otherwise. Assumes that the person was born before the current date
def isRecentBirth(person):
	# Gets the persons birthday
	birth = getDate(person['BIRT'])
	today = datetime.today()
	# 30 days is inclusive
	return (today - birth).days <= 30

class TestRecentBirths(unittest.TestCase):

	# Tests a person who was born in the last 30 days
	def test_recent_birth(self):
		today = datetime.today()
		strToday = today.strftime('%d %b %Y')
		individual = { 'NAME': 'Jordan Tantuico', 'BIRT': strToday}
		self.assertTrue(isRecentBirth(individual))

	# Tests a person who was not born in the last 30 days
	def test_not_recent_birth(self):
		today = datetime.today()
		thirtyOneDays = timedelta(days=31)
		thirtyOneDaysAgo = today - thirtyOneDays
		strThirtyOneDaysAgo = thirtyOneDaysAgo.strftime('%d %b %Y')
		individual = { 'NAME': 'Jordan Tantuico', 'BIRT': strThirtyOneDaysAgo}
		self.assertFalse(isRecentBirth(individual))

	# Tests a person who was born exactly 30 days ago
	def test_born_exactly_30_days_ago(self):
		today = datetime.today()
		thirtyDays = timedelta(days=30)
		thirtyDaysAgo = today - thirtyDays
		strThirtyDaysAgo = thirtyDaysAgo.strftime('%d %b %Y')
		individual = { 'NAME': 'Jordan Tantuico', 'BIRT': strThirtyDaysAgo}
		self.assertTrue(isRecentBirth(individual))

if __name__ == '__main__':
	unittest.main()