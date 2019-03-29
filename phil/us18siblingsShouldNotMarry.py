import unittest

#Parents should not marry any of their children
'''Returns true if children in family are not married to siblings, false if child is'''
def siblingsShouldNotMarry(individuals, families):
    isTrue = True
    for family in families:
        if 'CHIL' in families[family]:
            if len(families[family]['CHIL']) > 1:
                children = families[family]['CHIL']
                for child in children:
                    if child in individuals:
                        if 'FAMS' in individuals[child]:
                            famsValue = individuals[child]['FAMS']
                            husband = families[famsValue]['HUSB']
                            wife = families[famsValue]['WIFE']
                            if husband == child and wife in children:
                                isTrue = False
                                print("Error: US18: Child " + child + " and sibling " + wife + " are married")
                            if wife == child and husband in children:
                                isTrue = False
                                print("Error: US18: Child " + child + " and sibling " + husband + " are married")
    return isTrue

class Testus18siblingsShouldNotMarry(unittest.TestCase):
#test when only child in family
    def test_Normal_family(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940', 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'jc', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        self.assertTrue(siblingsShouldNotMarry(individuals, families))

#test when child is has sibling but is not married
    def test_not_married(self):
        individuals = {'de': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT': '1 JUN 1980'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940', 'FAMC': 'f2', 'FAMS' : 'f3', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}, 'bb': {'BIRT': '1 FEB 1940', 'FAMC': 'f2', 'NAME': 'Jil Doe', 'SEX': 'F', 'DEAT': '1 JUN 2010'}}
        families =  {'f2': {'HUSB': 'de', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa', 'bb']},'f3': {'HUSB': 'aa', 'WIFE': 'qw', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961'}}
        self.assertTrue(siblingsShouldNotMarry(individuals, families))

#test when child is married to sibling
    def test_married(self):
        individuals = {'de': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT': '1 JUN 1980'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940', 'FAMC': 'f2', 'FAMS' : 'f3', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}, 'bb': {'BIRT': '1 FEB 1940', 'FAMC': 'f2', 'NAME': 'Jil Doe', 'SEX': 'F', 'DEAT': '1 JUN 2010'}}
        families =  {'f2': {'HUSB': 'de', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa', 'bb']},'f3': {'HUSB': 'aa', 'WIFE': 'bb', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961'}}
        self.assertFalse(siblingsShouldNotMarry(individuals, families))

if __name__ == '__main__':
	unittest.main()








