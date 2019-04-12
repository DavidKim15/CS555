import unittest
'''Us11: No Bigamy. Check all individuals to see if they are involved in multiple marriages Returns true if individuals is not involved in multiple marriages,
Returns false if individual is involved in multiple marriages'''
def noBigamy(individuals, families):
    isTrue = True
    for indID in individuals:
        count = 0
        for famID in families:
            if indID == families[famID]['HUSB'] or indID == families[famID]['WIFE']:
                if 'DIV' not in families[famID]:
                    count = count + 1
            if count >= 2:
                print("Error: US11: Person " + indID + " is involved in multiple marriages")
                isTrue = False
                break
    return isTrue

class TestUS23UniqueNamesAndBD(unittest.TestCase):
    #test for when individuals are not involved in bigamy
    def test_normal_gedcom_file(self):
        individuals = {'de' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ab': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940','FAMS':'f4' , 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}, 'ac': {'BIRT': '1 FEB 1940','FAMS':'f4' , 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'de', 'WIFE': 'ac', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1961', 'CHIL': ['aa']}}
        self.assertTrue(noBigamy(individuals, families))
    #test for when individuals are involved in two marriage but divorced in one
    def test_div_in_family(self):
        individuals = {'de' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ab': {'BIRT': '1 FEB 1900', 'FAMS': 'f4', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940','FAMS':'f2' , 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960', 'DIV': '1 JUN 1959'}, 'f2': {'HUSB': 'de', 'WIFE': 'aa', 'MARR': '1 JUN 1960', 'CHIL': ['aa']}}
        self.assertTrue(noBigamy(individuals, families))

    #test for when individuals are involved in two marriage
    def test_bigamy_in_family(self):
        individuals = {'de' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ab': {'BIRT': '1 FEB 1900', 'FAMS': 'f4', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940','FAMS':'f2' , 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        families = {'f4': {'HUSB': 'de', 'WIFE': 'ab', 'MARR': '1 JUN 1960'}, 'f2': {'HUSB': 'de', 'WIFE': 'aa', 'MARR': '1 JUN 1960', 'CHIL': ['aa']}}
        self.assertFalse(noBigamy(individuals, families))


if __name__ == '__main__':
	unittest.main()
            
