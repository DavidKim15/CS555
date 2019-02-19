# This is a program that tests US21: Correct gender roles for marriages
# (Husband is a male and wife is a female)

import unittest

'''Function that tests whether the husband in a family is male and the wife is 
female, assumes there is a husband and wife in the family'''
def correctGenderRoles(family, individuals):
	# Gets husband and wife ID
	husbandId = family['HUSB']
	wifeId = family['WIFE']
	correctRoles = [True,True]
	# Checks if husband is male
	if individuals[husbandId]['SEX'] != 'M':
		correctRoles[0] = False
	# Checks if wife is female
	if individuals[wifeId]['SEX'] != 'F':
		correctRoles[1] = False
	return correctRoles

'''Testing class that runs several tests on US21'''
class TestCorrectGenderRoles(unittest.TestCase):

	# Tests a standard family where the husband is male and the wife is female
	def test_standard_family(self):
		husbando = {'NAME': 'Husbando', 'SEX': 'M'}
		waifu = {'NAME': 'Waifu', 'SEX': 'F'}
		individuals = {'h': husbando, 'w': waifu}
		family = {'HUSB': 'h', 'WIFE': 'w'}
		self.assertEqual([True,True],correctGenderRoles(family, individuals))

	# Tests when the husband of a family is female
	def test_husband_is_female(self):
		husbando = {'NAME': 'Husbando', 'SEX': 'F'}
		waifu = {'NAME': 'Waifu', 'SEX': 'F'}
		individuals = {'h': husbando, 'w': waifu}
		family = {'HUSB': 'h', 'WIFE': 'w'}
		self.assertEqual([False,True],correctGenderRoles(family, individuals))

	# Tests when the wife of a family is male
	def test_wife_is_male(self):
		husbando = {'NAME': 'Husbando', 'SEX': 'M'}
		waifu = {'NAME': 'Waifu', 'SEX': 'M'}
		individuals = {'h': husbando, 'w': waifu}
		family = {'HUSB': 'h', 'WIFE': 'w'}
		self.assertEqual([True,False],correctGenderRoles(family, individuals))

	# Tests when both partners have the opposite gender
	def test_role_reversal(self):
		husbando = {'NAME': 'Husbando', 'SEX': 'F'}
		waifu = {'NAME': 'Waifu', 'SEX': 'M'}
		individuals = {'h': husbando, 'w': waifu}
		family = {'HUSB': 'h', 'WIFE': 'w'}
		self.assertEqual([False,False],correctGenderRoles(family, individuals))

if __name__ == '__main__':
	unittest.main()