from datetime import datetime
import unittest
# for id in individuals:
#     boolean = birthBeforeMarriage(individuals[id], families)
#     if boolean = false:
#         print("Error: US02 Marriage Occurs in individual "+ id + " before Birth")
'''Returns true when birth occurs before marriage, and false when birth occurs after marriage'''
def birthBeforeMarriage(individual, families):
    if 'FAMS' in individual :
        famsValue = individual['FAMS']
        if 'MARR' in families[famsValue]:
            marriage = datetime.strptime(families[famsValue]['MARR'], '%d %b %Y')
            birth = datetime.strptime(individual['BIRT'], '%d %b %Y')
            if birth > marriage:
                return False
            else:
                return True
        else:
            print("User Story 02: Error in family, no Marriage Date")
            return True
    else:
        return True


class TestUS02BirthBeforeMarriage(unittest.TestCase):
    #test for when marriage occurs after birth
    def test_birth_before_marriage(self):
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'jc', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        individual = {'NAME': 'John/Doe/', 'SEX': 'F', 'BIRT': '1 JAN 1930', 'DEAT': '01 FEB 1940', 'FAMC': 'f2', 'FAMS': 'f4'}
        self.assertTrue(birthBeforeMarriage(individual, families))

    #test for when marriage occurs before birth
    def test_birth_after_marriage(self):
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'jc', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        individual = {'NAME': 'John/Doe/', 'SEX': 'F', 'BIRT': '1 JAN 1990', 'DEAT': '01 FEB 1940', 'FAMC': 'f2', 'FAMS': 'f4'}
        self.assertFalse(birthBeforeMarriage(individual, families))

    #test for when no FAMS tag is present in individual
    def test_birth_without_marriage(self):
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'jc', 'WIFE': 'ce', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        individual = {'NAME': 'John/Doe/', 'SEX': 'F', 'BIRT': '1 JAN 1990', 'DEAT': '01 FEB 1940', 'FAMC': 'f2'}
        self.assertTrue(birthBeforeMarriage(individual, families))
    


if __name__ == '__main__':
	unittest.main()