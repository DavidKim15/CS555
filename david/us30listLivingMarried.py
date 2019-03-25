import unittest

individuals = {
            'jd': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '31 DEC 2000',
                    'MARR': '31 DEC 2000',
                    'DIV': '31 DEC 2000',
                    'DEAT': '31 DEC 2000'}, 
            'jc': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '31 DEC 2000',
                    'MARR': '31 DEC 2000',
                    'DIV': '31 DEC 2000'}, 
            'ce': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '31 DEC 1950',
                    'DEAT': '2 JAN 2000',
                    'MARR': '1 JAN 1970'}, 
            'aa': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'BIRT': '31 DEC 1950',
                    'MARR': '2 JAN 2000'},
            }

def listLivingMarried(individuals):
    list_married = [] # list of ids
    for id in individuals:
        if 'MARR' in individuals[id] and 'DIV' not in individuals[id] and 'DEAT' not in individuals[id]:
            list_married.append(id)
    return list_married
class TestUS30(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertEqual(1,len(listLivingMarried(individuals)))
    def test_f2(self):
        self.assertIn('aa',listLivingMarried(individuals))
if __name__ == '__main__':
    unittest.main()