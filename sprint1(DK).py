import unittest

# male last name, returns bool
def US16(family, individuals):
    if 'HUSB' in family:
        hubby_lastname = individuals[family['HUSB']]['NAME'].split(" ",2)[1]
    else:
        return True
    if 'WIFE' in family:
        wifey_lastname = individuals[family['WIFE']]['NAME'].split(" ",2)[1]
    if 'CHIL' in family:
        child_lastnames = []
        for cid in family['CHIL']:
            child_ids.append(individuals[cid]['NAME'].split(" ",2)[1])
    print(hubby_lastname)
    print(wifey_lastname)
    print(child_lastnames)
# list of deceased people, returns list
def US29(individuals):
    pass
class TestUS16(unittest.TestCase):
    def setUp(self):
        pass
    def test_jordie_is_alive(self):
        jordie = {'NAME':'Jordan Tantuico', 'BIRT':'25 APR 1998'}
        self.assertTrue(methodname(jordie))

if __name__ == '__main__':
    
    # unittest.main()