import unittest
from datetime import datetime

# Returns True if the child is an orphan (both parents dead) and False otherwise
def isOrphan(child, mom, dad):
	# Dead children are not considered
	if 'DEAT' in child:
		return False
	# Calculates the child's age
	birthdate = datetime.strptime(child['BIRT'], '%d %b %Y')
	present = datetime.now()
	age = (present - birthdate).days/365
	# If the child is younger than 18 and both parents are dead, child is an orphan
	if age < 18 and 'DEAT' in mom and 'DEAT' in dad:
		return True
	# Otherwise, he is not
	return False

'''Testing class to detect orphans in a gedcom file'''
class TestIsOrphan(unittest.TestCase):

	# Tests a living child with both parents living
	def test_child_both_parents_living(self):
		child = { 'NAME': 'Jordan Tantuico', 'BIRT': '2 FEB 2010'}
		mom = {'NAME': 'Irene Tantuico', 'BIRT': '2 MAR 1965'}
		dad = {'NAME': 'Sam Tantuico', 'BIRT': '24 APR 1967'}
		self.assertFalse(isOrphan(child,mom,dad))

	# Tests a child with only one deceased parent
	def test_child_one_parent_dead(self):
		child = { 'NAME': 'Jordan Tantuico', 'BIRT': '2 FEB 2010'}
		mom = {'NAME': 'Irene Tantuico', 'BIRT': '2 MAR 1965', 'DEAT': '20 FEB 2019'}
		dad = {'NAME': 'Sam Tantuico', 'BIRT': '24 APR 1967'}
		self.assertFalse(isOrphan(child,mom,dad))

	# Tests a child with both parents dead
	def test_child_both_parents_dead(self):
		child = { 'NAME': 'Jordan Tantuico', 'BIRT': '2 FEB 2010'}
		mom = {'NAME': 'Irene Tantuico', 'BIRT': '2 MAR 1965', 'DEAT': '20 FEB 2019'}
		dad = {'NAME': 'Sam Tantuico', 'BIRT': '24 APR 1967', 'DEAT': '20 FEB 2019'}
		self.assertTrue(isOrphan(child,mom,dad))

	# Tests an adult with both parents dead
	def test_adult_both_parents_dead(self):
		adult = { 'NAME': 'Jordan Tantuico', 'BIRT': '25 APR 1998'}
		mom = {'NAME': 'Irene Tantuico', 'BIRT': '2 MAR 1965', 'DEAT': '20 FEB 2019'}
		dad = {'NAME': 'Sam Tantuico', 'BIRT': '24 APR 1967', 'DEAT': '20 FEB 2019'}
		self.assertFalse(isOrphan(adult,mom,dad))

	# Deceased children should not be considered orphans
	def test_dead_child(self):
		child = { 'NAME': 'Jordan Tantuico', 'BIRT': '25 APR 1998', 'DEAT': '20 FEB 2019'}
		mom = {'NAME': 'Irene Tantuico', 'BIRT': '2 MAR 1965', 'DEAT': '20 FEB 2019'}
		dad = {'NAME': 'Sam Tantuico', 'BIRT': '24 APR 1967', 'DEAT': '20 FEB 2019'}
		self.assertFalse(isOrphan(child,mom,dad))

if __name__ == '__main__':
	unittest.main()