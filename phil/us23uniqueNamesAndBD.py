import unittest
'''Checks file to see if any users have same name and birthdate, returns true if there are none, returns false if there are'''
def uniqueNamesAndBD(individuals):
    isTrue = True
    for indID in individuals:
        indName = individuals[indID]['NAME']
        indBD = individuals[indID]['BIRT']
        count = 0
        for indCurrent in individuals:
            if individuals[indCurrent]['NAME'] == indName and individuals[indCurrent]['BIRT'] == indBD:
                count = count + 1
            if count > 1:
                print("Error: US23: More than one user with name " + indName + " and birth date " + indBD + " exist")
                isTrue = False
                break
    return isTrue
class TestUS23UniqueNamesAndBD(unittest.TestCase):
    #test for when individuals all have different names and birthdates
    def test_normal_gedcom_file(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1940','FAMS':'f4' , 'FAMC': 'f2', 'NAME': 'Jack Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        self.assertTrue(uniqueNamesAndBD(individuals))
    #test for when two people have the same name but different birthdates
    def test_when_name_same_not_bd(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1990','FAMS':'f4' , 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        self.assertTrue(uniqueNamesAndBD(individuals))
    #test for when two people have the same birthdate but different names
    def test_when_bd_same_name_diff(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'Jane Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1990','FAMS':'f4' , 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        self.assertTrue(uniqueNamesAndBD(individuals))

    #test for when two people have the same birthdate and same names
    def test_name_same_bd_same(self):
        individuals = {'jc' : {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT' : '1 NOV 1999'},'ce': {'BIRT': '1 FEB 1900', 'FAMS': 'f2', 'NAME': 'John Doe', 'SEX': 'F', 'DEAT': '1 JUN 1980'}, 'aa': {'BIRT': '1 FEB 1990','FAMS':'f4' , 'FAMC': 'f2', 'NAME': 'John Doe', 'SEX': 'M', 'DEAT': '1 JUN 2010'}}
        self.assertFalse(uniqueNamesAndBD(individuals))
if __name__ == '__main__':
	unittest.main()
