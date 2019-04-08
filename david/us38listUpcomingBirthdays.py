import unittest
from datetime import datetime

# List all living people in a GEDCOM file whose birthdays occur in the next 30 days

def getDate(date):
	return datetime.strptime(date, '%d %b %Y')

individuals = {
            'jd': {'NAME': 'Jimmy /Supers/',
                    'SEX': 'M',
                    'BIRT': '31 DEC 2099'}, 
            'jc': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '15 APR 2019'}, 
            'ce': {'NAME': 'Jaimie /Connors/',
                    'SEX': 'F', 
                    'BIRT': '6 APR 2019'}, 
            'aa': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M',
                    'BIRT': '4 MAR 2019'},
            'ab': {'NAME': 'Aaron /Pineapple/', 
                    'SEX': 'M',
                    'BIRT': '31 DEC 2099'},
            'ac': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M',
                    'BIRT': '31 DEC 2099'}
            }
def listUpcomingBirthdays(individuals):
    ret = []
    today = datetime.today()
    for id in individuals:
        if 'BIRT' in individuals[id]:
            if (getDate(individuals[id]['BIRT']) - today).days <= 30 and (getDate(individuals[id]['BIRT']) - today).days >= -1:
                ret.append(id)
    return ret

class TestUS38(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertEqual(2,len(listUpcomingBirthdays(individuals)))
    def test_f2(self):
        self.assertTrue('jc' in listUpcomingBirthdays(individuals))
    def test_f3(self):
        self.assertTrue('ce' in listUpcomingBirthdays(individuals))
    def test_f4(self):
        self.assertFalse('aa' in listUpcomingBirthdays(individuals))

if __name__ == '__main__':
    unittest.main()