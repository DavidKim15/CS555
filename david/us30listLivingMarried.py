import unittest

families = {
            'f1': {'HUSB': 'j1', 
                    'WIFE': 'c1',  
                    'MARR': '1 JUN 1960'},
            'f2': {'HUSB': 'j2', 
                    'WIFE': 'c2',  
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},      
            }

def listLivingMarried(families):
    list_married = [] # list of ids
    for id in families:
        if 'MARR' in families[id] and 'DIV' not in families[id] and 'DEAT' not in families[id]:
            list_married.append(families[id]['HUSB'])
            list_married.append(families[id]['WIFE'])
    return list_married
class TestUS30(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertEqual(2,len(listLivingMarried(families)))
    def test_f2(self):
        self.assertIn('j1',listLivingMarried(families))
        self.assertIn('c1',listLivingMarried(families))
if __name__ == '__main__':
    unittest.main()