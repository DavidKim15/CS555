import unittest
from datetime import datetime, timedelta

''' Converts a string into a date object. The parameter date is the date string 
	in the form "23 APR 2019" '''
def getDate(date):
	return datetime.strptime(date, '%d %b %Y')

# Returns True if the person record has died in the past 30 days, returns 
# False otherwise. Assumes that the person has died before the current date
# or the person is still living
def isRecentDeath(person):
	# Person is still alive
	if 'DEAT' not in person:
		return False
	# Gets the persons death day
	death = getDate(person['DEAT'])
	today = datetime.today()
	# 30 days is inclusive
	return (today - death).days <= 30

class TestRecentDeaths(unittest.TestCase):

	# Tests a person who is still alive
	def test_living(self):
		individual = { 'NAME': 'Jordan Tantuico', 'BIRT': '1 JAN 2000'}
		self.assertFalse(isRecentDeath(individual))

	# Tests a person who died in the last 30 days
	def test_recent_death(self):
		today = datetime.today()
		strToday = today.strftime('%d %b %Y')
		individual = { 'NAME': 'Jordan Tantuico', 'DEAT': strToday}
		self.assertTrue(isRecentDeath(individual))

	# Tests a person who died over 30 days
	def test_not_recent_death(self):
		today = datetime.today()
		thirtyOneDays = timedelta(days=31)
		thirtyOneDaysAgo = today - thirtyOneDays
		strThirtyOneDaysAgo = thirtyOneDaysAgo.strftime('%d %b %Y')
		individual = { 'NAME': 'Jordan Tantuico', 'DEAT': strThirtyOneDaysAgo}
		self.assertFalse(isRecentDeath(individual))

	# Tests a person who died exactly 30 days ago
	def test_died_exactly_30_days_ago(self):
		today = datetime.today()
		thirtyDays = timedelta(days=30)
		thirtyDaysAgo = today - thirtyDays
		strThirtyDaysAgo = thirtyDaysAgo.strftime('%d %b %Y')
		individual = { 'NAME': 'Jordan Tantuico', 'DEAT': strThirtyDaysAgo}
		self.assertTrue(isRecentDeath(individual))

	# Tests a person who died after the current date
	def test_died_after_present(self):
		today = datetime.today()
		thirtyDays = timedelta(days=1)
		thirtyDaysAgo = today - thirtyDays
		strThirtyDaysAgo = thirtyDaysAgo.strftime('%d %b %Y')
		individual = { 'NAME': 'Jordan Tantuico', 'DEAT': strThirtyDaysAgo}
		self.assertTrue(isRecentDeath(individual))

if __name__ == '__main__':
	unittest.main()