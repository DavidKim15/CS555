from datetime import datetime
import unittest

'''Returns true when family is married before divorce, false if divorced before marriage or if divorced but
not married '''
def marriageBeforeDivorce(family) : 
    errorList = []
    if 'DIV' in family :
        if 'MARR' in family:
            marriage = datetime.strptime(family['MARR'],'%d %b %Y')
            divorce = datetime.strptime(family['DIV'], '%d %b %Y')
            if marriage > divorce :
                # print("Error: Family: " + id + " Divorced " + families[id]['DIV'] + " Before Marriage " + families[id]['MARR'])
                # errorList.append(individuals[id])
                return False
            else :
                return True
        else :
            # errorList.append(individuals[id])
            # print("Error: Family: " + id + " Divorced " + families[id]['DIV'] + " Before Marriage" + families[id]['MARR'])
            return False
    else:
        if 'MARR' in family :
            return True
        else :
            return False
    # return errorList
'''testing class that tests user story 4, marriage before divorce'''
class TestMarriageBeforeDivorce(unittest.TestCase):

    #test for family that is divorced before marriage
    def test_divorce_before_marriage(self) :
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1963'}
        self.assertFalse(marriageBeforeDivorce(family))

    #test for family that is divorced after marriage
    def test_divorce_after_marriage(self) :
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce', 'MARR': '1 JUN 1945'}
        self.assertTrue(marriageBeforeDivorce(family))

    #test for family that is married but not divorced
    def test_marriage_but_no_divorce(self) :
        family = {'HUSB': 'jc', 'WIFE' : 'ce', 'MARR': '1 JUN 1945'}
        self.assertTrue(marriageBeforeDivorce(family))

    #test for family that is divorced without being married
    def test_divorce_without_married(self) :
        family = {'HUSB': 'jc', 'DIV': '1 JUN 1961', 'WIFE' : 'ce'}
        self.assertFalse(marriageBeforeDivorce(family))
    
    #test for family that is not married or divorced
    def test_divorce_and_not_married(self) :
        family = {'HUSB': 'jc', 'WIFE' : 'ce'}
        self.assertFalse(marriageBeforeDivorce(family))
    


if __name__ == '__main__':
	unittest.main()

