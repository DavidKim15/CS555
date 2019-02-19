import unittest

individuals = {
            'jd': {'NAME': 'Jimmy /Supers/',
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'}, 
            'jc': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'DEAT': '31 DEC 2099'}, 
            'ce': {'NAME': 'Jaimie /Connors/',
                    'SEX': 'F', 
                    'DEAT': '31 DEC 2099'}, 
            'aa': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'},
            'ab': {'NAME': 'Aaron /Pineapple/', 
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'},
            'ac': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'}
            }
families = {'f1': {'HUSB': 'jc', 
                    'WIFE': 'ce', 
                    'CHIL': ['aa','ac'], 
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},
            'f2': {'HUSB': 'jc', 
                    'WIFE': 'ce', 
                    'CHIL': ['aa'], 
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},
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
def maleLastName(family, individuals):
    child_lastnames = []
    if 'HUSB' in family:
        hubby_lastname = individuals[family['HUSB']]['NAME'].split(" ",2)[1]
        if 'CHIL' in family:
            for cid in family['CHIL']:
                if individuals[cid]['SEX'] == 'M':
                    child_lastnames.append(individuals[cid]['NAME'].split(" ",2)[1])
    else:  
        return True
    for c_ln in child_lastnames:
        if hubby_lastname != c_ln:
            return False
    return True

class TestUS16(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertTrue(maleLastName(families['f1'],individuals))
    def test_f2(self):
        self.assertTrue(maleLastName(families['f2'],individuals))
    def test_f3(self):
        self.assertFalse(maleLastName(families['f3'],individuals))
    def test_f4(self):
        self.assertTrue(maleLastName(families['f4'],individuals))
    def test_f5(self):
        self.assertTrue(maleLastName(families['f5'],individuals))

if __name__ == '__main__':
    unittest.main()