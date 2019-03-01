# Jordan Tantuico
# I pledge my honor that I have abided by the Stevens Honor System
# This is a program that tests the functionality of US03: Birth before death

import unittest
from datetime import datetime

''' Converts a string into a date object. The parameter date is the date string 
	in the form "23 APR 2019" '''
def getDate(date):
	return datetime.strptime(date, '%d %b %Y')

'''Returns True when person's birth is before their death. Returns False
   otherwise. Parameter person is a dictionary object with several GEDCOM 
   tags as keys. The person is assumed to have all the required tags (like BIRT)
   '''
def birthBeforeDeath(person):
	# Person is still living, doesn't have DEAT tag
	if 'DEAT' not in person:
		return True
	# Obtains date values from person
	birthdate = getDate(person['BIRT'])
	deathdate = getDate(person['DEAT'])
	# If birthdate is less than deathdate, that means birthdate is earlier
	return birthdate <= deathdate


'''Testing class that runs several tests on US03'''
class TestBirthBeforeDeath(unittest.TestCase):

	# Tests people who are still living
	def test_jordie_is_alive(self):
		# That's me!
		jordie = { 'NAME': 'Jordan Tantuico', 'BIRT': '25 APR 1998'}
		self.assertTrue(birthBeforeDeath(jordie))

	# Tests Nintendo services that died after they were born
	def test_rip_wii_shop(self):
		# RIP Wii Shop Channel, Press F
		# https://www.youtube.com/watch?v=SbFjfOA71x4
		wiiShop = { 'NAME': 'Wii Shop Channel', 'BIRT': '10 DEC 2006', 
		'DEAT': '30 JAN 2019'}
		self.assertTrue(birthBeforeDeath(wiiShop))

	# Tests bugs who died on the same day they were born
	def test_instantaneous_death(self):
		# These unfortunate insects only live for 24 hours, yet they are still
		# able to reproduce.
		mayfly = { 'NAME': 'Marty McMayfly', 'BIRT': '12 FEB 2019', 'DEAT': '12 FEB 2019'}
		self.assertTrue(birthBeforeDeath(mayfly))

	# Tests people who died before they were born
	def test_back_to_the_future(self):
		# In this alternate timeline, Marty dies when he goes to the past
		marty = { 'NAME': 'Marty McFly', 'BIRT': '12 JUN 1968', 'DEAT': '5 NOV 1955'}
		self.assertFalse(birthBeforeDeath(marty))

	# Tests the helper function getDate
	def test_get_date(self):
		# Leap year
		dateString = '29 FEB 2016'
		dateObject = datetime(2016, 2, 29)
		self.assertEqual(dateObject, getDate(dateString))

	# Tests two dates that are not the same
	def test_get_date2(self):
		# Leap year
		dateString = '29 FEB 2016'
		dateObject = datetime(2016, 2, 28)
		self.assertNotEqual(dateObject, getDate(dateString))


if __name__ == '__main__':
	unittest.main()