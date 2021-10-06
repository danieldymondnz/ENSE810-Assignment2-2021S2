'''
DBAgent Unit Testing
'''

from DBAgent import DBAgent
import unittest

class DBAgent_test(unittest.TestCase):

    def test_localTripStatus(self):
        self.dba = DBAgent(0, 0, 0)
        res = self.dba._queryLocalTripStatus()
        self.assertEqual(res, 1, 'No UID could be obtained')
        
if __name__ == '__main__':
    unittest.main()