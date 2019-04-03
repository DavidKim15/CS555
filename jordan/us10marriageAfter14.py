import unittest
from datetime import datetime, date

# Returns True if a marriage occurs at least 14 years after someone's birth date
# Returns False otherwise
def marriageAfter14(birthDate,marriageDate):
	ageAtMarriage = (marriageDate - birthDate).days/365
	if ageAtMarriage < 14:
		return False 
	return True 

class TestMarriageAfter14(unittest.TestCase):
	# Tests a marriage when someone was older than 14
	def test_marriage_after_14(self):
		birthDate = date(2000,1,1)
		marriageDate = date(2015,1,1)
		self.assertTrue(marriageAfter14(birthDate,marriageDate))
	# Tests a marriage when someone was younger than 14
	def test_marriage_before_14(self):
		birthDate = date(2000,1,1)
		marriageDate = date(2010,1,1)
		self.assertFalse(marriageAfter14(birthDate,marriageDate))
	# Tests a marriage when someone was 14 years old
	def test_marriage_at_14(self):
		birthDate = date(2000,1,1)
		marriageDate = date(2014,2,2)
		self.assertTrue(marriageAfter14(birthDate,marriageDate))

if __name__ == '__main__':
	unittest.main()