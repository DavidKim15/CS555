import unittest

families = {'f1': {'HUSB': 'jc', 
                    'WIFE': 'ce', 
                    'CHIL': ['aa','ac'], 
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},
            'f2': {'HUSB': 'jc', 
                    'WIFE': 'ce', 
                    'CHIL': ['aa','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'], 
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},
            'f3': {'HUSB': 'jc', 
                    'WIFE': 'ce',  
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},
            'f4': {'HUSB':'jc',
                    'CHIL':[]
                  }
            }

def fewerThan15Sibs(family):
    if 'CHIL' in family:
        if len(family['CHIL']) > 15:
            return False
    return True
            
class TestUS15(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertTrue(fewerThan15Sibs(families['f1']))
    def test_f2(self):
        self.assertFalse(fewerThan15Sibs(families['f2']))
    def test_f3(self):
        self.assertTrue(fewerThan15Sibs(families['f3']))
    def test_f4(self):
        self.assertTrue(fewerThan15Sibs(families['f4']))
if __name__ == '__main__':
    unittest.main()