import unittest
from datetime import datetime
from datetime import timedelta

# List all living couples in a GEDCOM file whose marriage 
# anniversaries occur in the next 30 days

families = {'f1': {'HUSB': '1', 
                    'WIFE': '2', 
                    'CHIL': ['aa','ac'], 
                    'MARR': '1 JUN 1960', 
                    'DIV': '1 JUN 1961'},
            'f2': {'HUSB': '3', 
                    'WIFE': '4', 
                    'CHIL': ['aa','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15'], 
                    'MARR': '1 APR 1960', 
                    'DIV': '1 JUN 1961'},
            'f3': {'HUSB': '5', 
                    'WIFE': '6',  
                    'MARR': '20 APR 1960', 
                    'DIV': '1 JUN 1961'},
            'f4': {'HUSB':'7',
                    'CHIL':[]
                  }
            }

''' Converts a string into a date object. The parameter date is the date string 
	in the form "23 APR 2019" '''
def getDate(date):
    return datetime.strptime(date, '%d %b %Y')

def listUpcomingAnniversaries(families):
    list_upcom_ann = [] #list of pairs of id of couples [{1,2},{3,4}]
    curr_date = datetime.now()
    for id in families:
        if 'MARR' in families[id]: 
            marr_date = getDate(families[id]['MARR'])
            marr_date = marr_date.replace(year = curr_date.year)
            if curr_date + timedelta(days = 30) > marr_date:
                list_upcom_ann.append(id)
            # if ((marr_date - curr_date).days % 365) < 30:
            #     list_upcom_ann.append({families[id]['HUSB'], families[id]['WIFE']})
    return list_upcom_ann

class TestUS39(unittest.TestCase):
    def setUp(self):
        pass
    def test_f1(self):
        self.assertEqual(2,len(listUpcomingAnniversaries(families)))
    def test_f2(self):
        self.assertIn('f3',listUpcomingAnniversaries(families))
    def test_f3(self):
        self.assertIn('f2',listUpcomingAnniversaries(families))    
if __name__ == '__main__':
    unittest.main()
    # listUpcomingAnniversaries(families)