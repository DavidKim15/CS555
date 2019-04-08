import unittest
from datetime import datetime

# All dates should be legitimate dates for the months specified (e.g., 2/30/2015 is not legitimate)

def getDate(date):
	return datetime.strptime(date, '%d %b %Y')

individuals = {
            'jd': {'NAME': 'Jimmy /Supers/',
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'}, 
            'jc': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
					'MARR': '1010 FEB 2019',
                    'DEAT': '31 DEC 2099'}, 
			}
families = {'f1': {'HUSB': 'jc', 
                    'WIFE': 'ce', 
                    'CHIL': ['aa','ac'], 
                    'MARR': '32 JUN 1960', 
                    'DIV': '29 FEB 2012'},
            'f2': {'HUSB': 'jc', 
                    'WIFE': 'ce', 
                    'CHIL': ['aa'], 
                    'MARR': '50 JUN 1960', 
                    'DIV': '30 FEB 1961'},
            'f3': {'HUSB': 'jc', 
                    'WIFE': 'ce', 
                    'CHIL': ['ab'], 
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},
            'f4': {'WIFE':'ce',
                    'CHIL':['aa']
                  },
            'f5': {'HUSB':'jc',
                  }
            }
def rejectIllegitimateDates(checkFamOrInd):
	ret = []
	if 'BIRT' in checkFamOrInd:
		try:
			getDate(checkFamOrInd['BIRT'])
		except:
			ret.append('BIRT')
	if 'DEAT' in checkFamOrInd:
		try:
			getDate(checkFamOrInd['DEAT'])
		except:
			ret.append('DEAT')
	if 'MARR' in checkFamOrInd:
		try:
			getDate(checkFamOrInd['MARR'])
		except:
			ret.append('MARR')
	if 'DIV' in checkFamOrInd:
		try:
			getDate(checkFamOrInd['DIV'])
		except:
			ret.append('DIV')
	return ret
    
class TestUS42(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertEqual(1,len(rejectIllegitimateDates(families['f1'])))
    def test_f2(self):
        self.assertTrue('MARR' in rejectIllegitimateDates(families['f1']))
    def test_f3(self):
        self.assertEqual(2,len(rejectIllegitimateDates(families['f2'])))
    def test_f4(self):
        self.assertEqual(0, len(rejectIllegitimateDates(individuals['jd'])))
    def test_f5(self):
        self.assertEqual(0, len(rejectIllegitimateDates(families['f5'])))

if __name__ == '__main__':
    unittest.main()