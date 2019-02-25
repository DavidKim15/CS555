import unittest
from datetime import datetime

individuals = {
            'jd': {'NAME': 'Jimmy /Supers/',
                    'SEX': 'M',
                    'BIRT': '31 DEC 1950'}, 
            'jc': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '31 DEC 2000'}, 
            'ce': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '31 DEC 1950',
                    'DEAT': '2 JAN 2000',
                    'MARR': '1 JAN 1970'}, 
            'aa': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '31 DEC 1950',
                    'DEAT': '2 JAN 2000'},
            }
# over 30 never been married
def listLivingSingle(individuals):
    list_single = []
    for id in individuals:
        if 'BIRT' in individuals[id] and 'DEAT' not in individuals[id]:
            now = datetime.now()
            birthdate = datetime.strptime(individuals[id]['BIRT'], '%d %b %Y')
            diff = (now - birthdate).days/365
            if diff > 30:
                if 'MARR' not in individuals[id]:
                    list_single.append(id)
    return list_single
class TestUS31(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertEqual(1,len(listLivingSingle(individuals)))
    def test_f2(self):
        self.assertIn('jd',listLivingSingle(individuals))
if __name__ == '__main__':
    unittest.main()