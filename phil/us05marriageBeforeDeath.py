from datetime import datetime
import unittest

'''Returns true if couple is married before death, returns false if couple is married after death'''
def marriageBeforeDeath(families, individuals) : 
    husband = families['HUSB']
    wife = families['WIFE']
    if 'DEAT' in individuals[husband] :
        marriage = datetime.strptime(families['MARR'], '%d %b %Y')
        death = datetime.strptime(individuals[husband]['DEAT'], '%d %b %Y')
        if marriage > death :
            return False
    if 'DEAT' in individuals[wife] :
        marriage = datetime.strptime(families['MARR'], '%d %b %Y')
        death = datetime.strptime(individuals[wife]['DEAT'], '%d %b %Y')
        if marriage > death :
            return False
    return True

class TestMarriageBeforeDeath(unittest.TestCase):

    #test for marriage that occurs after husband's death
    def test_divorce_before_marriage_husb(self) :
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        individuals = {'jc' : {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '31 DEC 1950'},'ce': {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F'}}
        self.assertFalse(marriageBeforeDeath(family, individuals))

    #test for marriage that occurs after a wife's death
    def test_divorce_before_marriage_wife(self) :
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        individuals = {'jc' : {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M'},'ce': {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1959'}}
        self.assertFalse(marriageBeforeDeath(family, individuals))

    #test for normal marriage in with marriage occurs after death
    def test_divorce_before_marriage_normal(self) :
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        individuals = {'jc' : {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT': '1 JUN 1970'},'ce': {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}}
        self.assertTrue(marriageBeforeDeath(family, individuals))

    #test for when women is dead but marriage occurs before
    def test_divorce_before_marriage_normal_wife(self) :
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        individuals = {'jc' : {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M'},'ce': {'BIRT': '1 FEB 2000', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}}
        self.assertTrue(marriageBeforeDeath(family, individuals))
if __name__ == '__main__':
	unittest.main()
