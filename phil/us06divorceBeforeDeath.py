from datetime import datetime
import unittest
'''Returns true in normal situation, i.e. divorce occurs before death of both spouses, false when
divorce occurs after death of both spouses'''
def divorceBeforeDeath(family, individuals):
    husband = family['HUSB']
    wife = family['WIFE']
    if 'DIV' in family:
        if 'DEAT' in individuals[husband]:
            if 'DEAT' in individuals[wife] :
                husbandDeath = datetime.strptime(individuals[husband]['DEAT'], '%d %b %Y')
                wifeDeath = datetime.strptime(individuals[wife]['DEAT'], '%d %b %Y')
                divorce = datetime.strptime(family['DIV'], '%d %b %Y')
                if husbandDeath < divorce:
                    if wifeDeath < divorce:
                        return False
                    else: 
                        return True
                else:
                    return True
            else:
                return True
        else :
            return True
    else :
        return True

class Testus06DivorceBeforeDeath(unittest.TestCase):

#test when divorced prior to death of both husband and wife
    def test_Normal_divorce(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}}
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        self.assertTrue(divorceBeforeDeath(family,individuals))

#test when husband is deceased but wife is not
    def test_husband_death_not_wife(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F'}}
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        self.assertTrue(divorceBeforeDeath(family,individuals))

#test when husband and wife are both deceased before the divorce date
    def test_divorce_after_death(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F','DEAT': '1 JUN 1980'}}
        family = {'HUSB': 'jc', 'DIV': '1 JUN 2010', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        self.assertFalse(divorceBeforeDeath(family,individuals))

#test when husband and wife are both deceased but there is no divorce
    def test_no_divorce_after_death(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMC': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F','DEAT': '1 JUN 1980'}}
        family = {'HUSB': 'jc', 'WIFE' : 'ce', 'MARR': '1 JUN 1960'}
        self.assertTrue(divorceBeforeDeath(family,individuals))

if __name__ == '__main__':
	unittest.main()
