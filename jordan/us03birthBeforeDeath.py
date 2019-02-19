# Jordan Tantuico
# I pledge my honor that I have abided by the Stevens Honor System
# This is a program that tests the functionality of US03: Birth before death

import unittest
from datetime import datetime

'''Returns True when person's birth is before their death. Returns False
   otherwise'''
def birthBeforeDeath(person):
	if 'BIRT' not in person:
		return False
	# Person still living
	if 'DEAT' not in person:
		return True
	# Person died on same day of birth
	if person['BIRT'] == person['DEAT']:
		return False
	# Obtains date values from person
	birthdate = datetime.strptime(person['BIRT'], '%d %b %Y')
	deathdate = datetime.strptime(person['DEAT'], '%d %b %Y')
	# Compares birthdate with deathdate
	if birthdate < deathdate:
		return True
	return False
	

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
		self.assertFalse(birthBeforeDeath(mayfly))


	# Tests people who died before they were born
	def test_back_to_the_future(self):
		# In this alternate timeline, Marty dies when he goes to the past
		marty = { 'NAME': 'Marty McFly', 'BIRTH': '12 JUN 1968', 'DEAT': '5 NOV 1955'}
		self.assertFalse(birthBeforeDeath(marty))

	# Tests exos who don't have birthdays
	def test_no_birth(self):
		# RIP Cayde-6
		cayde6 = { 'NAME': 'Cayde-6', 'DEAT': '4 SEP 2018'}
		self.assertFalse(birthBeforeDeath(cayde6))

	# Tests inanimate objects that have no birth or death
	def test_chair(self):
		# It's just a chair
		chair = { 'NAME': 'Chair'}
		self.assertFalse(birthBeforeDeath(chair))


if __name__ == '__main__':
	unittest.main()