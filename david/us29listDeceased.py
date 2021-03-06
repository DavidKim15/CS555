# list of deceased people, returns list
import unittest

individuals = {
            'jd': {'NAME': 'Jimmy /Supers/',
                    'SEX': 'M'}, 
            'jc': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'DEAT': '19 FEB 2019'}, 
            'ce': {'NAME': 'Jaimie /Connors/',
                    'SEX': 'F', 
                    'DEAT': '31 DEC 2099'}, 
            'aa': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M'},
            'ab': {'NAME': 'Aaron /Pineapple/', 
                    'SEX': 'M',
                    'DEAT': '01 JAN 2000'},
            'ac': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M',
                    'DEAT': '18 FEB 2019'}
            }

# US29
def listDeceased(individuals):
	deceased_list = []
	for id in individuals:
		if 'DEAT' in individuals[id]:
			deceased_list.append(id)		
	return deceased_list

class TestUS29(unittest.TestCase):
	def setUp(self):
		pass
	def test_f1(self):
		self.assertIn('ac',listDeceased(individuals))
	def test_f3(self):
		self.assertEqual(4,len(listDeceased(individuals)))
	def test_f4(self):
		self.assertNotEqual(len(individuals),len(listDeceased(individuals)))

if __name__ == '__main__':
    unittest.main()
