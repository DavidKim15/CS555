import unittest
from datetime import datetime

def getDate(date):
	return datetime.strptime(date, '%d %b %Y')

individuals = {
            'm1': {'NAME': 'Jimmy /Supers/',
                    'SEX': 'M',
                    'BIRT': '15 FEB 1980'}, 
            'w1': {'NAME': 'Jenna /Connors/',
                    'SEX': 'M', 
                    'BIRT': '1 JUL 2000'}, 
            'm2': {'NAME': 'John /Obama/',
                    'SEX': 'M',
                    'BIRT': '1 JAN 2000'}, 
            'w2': {'NAME': 'Kayla /Manna/',
                    'SEX': 'M',
                    'BIRT': '1 JAN 2004'},  
        	'm3': {'NAME': 'John /Obama/',
                    'SEX': 'M',
                    'BIRT': '1 JAN 2008'}, 
            'w3': {'NAME': 'Kayla /Manna/',
                    'SEX': 'M',
                    'BIRT': '15 FEB 1980'},         
			}
families = {'f1': {'HUSB': 'm1', 
                    'WIFE': 'w1', 
                    'CHIL': ['aa','ac'], 
                    'MARR': '1 JAN 2010'},
            'f2': {'HUSB': 'm2', 
                    'WIFE': 'w2',
                    'MARR': '1 JAN 2010', 
                    'DIV': '30 FEB 1961'},
			'f3': {'HUSB': 'm3', 
                    'WIFE': 'w3',
                    'MARR': '1 JAN 2010', 
                    'DIV': '30 FEB 1961'}
            }
def listLargeAgeDifferences(families, individuals):
	ret = []
	for fid in families:
		current_fam = families[fid]
		man_id = current_fam['HUSB']
		woman_id = current_fam['WIFE']

		marriage_date = getDate(current_fam['MARR'])
		man_birthdate = getDate(individuals[man_id]['BIRT'])
		woman_birthdate = getDate(individuals[woman_id]['BIRT'])
		if (marriage_date-man_birthdate).days/365 > 2*(marriage_date-woman_birthdate).days/365:
			ret.append(fid)
		elif (marriage_date-woman_birthdate).days/365 > 2*(marriage_date-man_birthdate).days/365:
			ret.append(fid)
	return ret
    
class Test34(unittest.TestCase):
	def setUp(self):
		pass
	def test_f1(self):
		self.assertEqual(2,len(listLargeAgeDifferences(families, individuals)))
	def test_f2(self):
		self.assertTrue('f1' in listLargeAgeDifferences(families, individuals))
	def test_f3(self):
		self.assertTrue('f3' in listLargeAgeDifferences(families, individuals))

if __name__ == '__main__':
    unittest.main()