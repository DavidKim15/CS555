import unittest

#Parents should not marry any of their children
'''Prints all cases when children are married to parents, returns true if there are no cases, false if a case exists'''
def noMarriagesToChildren(individuals, families):
    isTrue = True
    for id in individuals:
        if 'FAMC' in individuals[id]:
            famcValue = individuals[id]['FAMC']
            mother = families[famcValue]['WIFE']
            father = families[famcValue]['HUSB']
            if id == father or id == mother :
                print("Error: US17: Child " + id  + " in family " + famcValue + " is married to a parent")
                isTrue = False
            if 'FAMS' in individuals[id]:
                famsValue = individuals[id]['FAMS']
                if families[famsValue]['HUSB'] == id:
                    if families[famsValue]['WIFE'] == mother:
                        print("Error: US17: Child " + id  + " in family " + famcValue + " is married to a parent")
                        isTrue = False
                if families[famsValue]['WIFE'] == id:
                    if families[famsValue]['HUSB'] == father:
                        print("Error: US17: Child " + id  + " in family " + famcValue + " is married to a parent")
                        isTrue = False
    return isTrue


class Testus17noMarriagesToChildren(unittest.TestCase):
#test when family is normal
    def test_Normal_family(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940', 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'jc', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        self.assertTrue(noMarriagesToChildren(individuals, families))

#test when child is married to parent within the same family
    def test_within_family(self):
        individuals = {'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940', 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        families =  {'f2': {'HUSB': 'aa', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        self.assertFalse(noMarriagesToChildren(individuals, families))

#test when child is married to parent in a different family
    def test_out_of_family(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940','FAMS':'f4' , 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        families = {'f4': {'HUSB': 'aa', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'jc', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        self.assertFalse(noMarriagesToChildren(individuals, families))

if __name__ == '__main__':
	unittest.main()