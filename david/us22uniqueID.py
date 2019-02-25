import unittest

individuals = {
            'jd': {'NAME': 'Jimmy /Supers/',
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'}, 
            'jc': {'NAME': 'Jimmy /Connors/',
                    'SEX': 'M',  
                    'DEAT': '31 DEC 2099'}, 
            'ce': {'NAME': 'Jaimie /Connors/',
                    'SEX': 'F', 
                    'DEAT': '31 DEC 2099'}, 
            'aa': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'},
            'ab': {'NAME': 'Aaron /Pineapple/', 
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'},
            'ac': {'NAME': 'Aaron /Connors/', 
                    'SEX': 'M',
                    'DEAT': '31 DEC 2099'}
            }

def uniqueID(id,individuals):
    if id in individuals:
        return True
    else:
        return False
class TestUS22(unittest.TestCase):
    pass
if __name__ == '__main__':
    unittest.main()