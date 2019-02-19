import unittest
from datetime import datetime

def lessThan150(individual):
	if 'DEAT' in individual:
		birthdate = datetime.strptime(individual['BIRT'], '%d %b %Y')
		deathdate = datetime.strptime(individual['DEAT'], '%d %b %Y')
		if (deathdate - birthdate).days/365 < 150:
			return True
		else:
			return False
	else:
		now = datetime.now()
		birthdate = datetime.strptime(individual['BIRT'], '%d %b %Y')
		if (now - birthdate).days/365 < 150:
			return True
		else:
			return False

class TestLessThan150(unittest.TestCase):

	# Testing the death of Jesus Christ
	def test_dead_guy_whos_150(self):
		jesus = { 'NAME': "Jesus", 'BIRT': '25 DEC 0001', 'DEAT': '3 APR 0250'}
		self.assertFalse(lessThan150(jesus))

	# Testing Isaac Newton
	def test_dead_guy_whos_not_150(self):
		isaac = {'NAME': 'Isaac Newton', 'BIRT': '4 JAN 1643', 'DEAT': '31 MAR 1727'}
		self.assertTrue(lessThan150(isaac))

	# Testing Barack Obama
	def test_living_whos_not_150(self):
		obama = {'NAME': 'Barack Obama', 'BIRT': '4 AUG 1961'}
		self.assertTrue(lessThan150(obama))

	# Testing Dalai Lama
	def test_living_whos_150(self):
		dalaiLama = {'NAME': 'Dalai Lama', 'BIRT': '6 JUL 1860'}
		self.assertFalse(lessThan150(dalaiLama))

if __name__ == '__main__':
	unittest.main()