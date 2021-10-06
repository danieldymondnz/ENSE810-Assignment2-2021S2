'''
DBAgent Unit Testing
'''

from DBAgent import DBAgent
import time
import unittest

class DBAgent_test(unittest.TestCase):

    localDBConfig = {
        "fileLocation": "App/testDB.db"
    }

    def test_queryLocalTripSyncStatus(self):
        self.dba = DBAgent(0, DBAgent_test.localDBConfig, 0)
        self.dba._initialSetup()
        time.sleep(100)
        res = self.dba._queryLocalTripSyncStatus()
        self.dba._cleanup()
        time.sleep(100)
        self.assertEqual(res, 1, 'No UID could be obtained')

    def test_queryLocalTripCurrentID(self):
        self.dba = DBAgent(0, DBAgent_test.localDBConfig, 0)
        self.dba._initialSetup()
        res = self.dba._queryLocalTripCurrentID()
        self.assertEqual(res, [1, 0], 'Current Trip details could be obtained')

    def test_setLocalTripCurrentComplete(self):
        self.dba = DBAgent(0, DBAgent_test.localDBConfig, 0)
        self.dba._initialSetup()
        self.dba._setLocalTripCurrentComplete()
        res = self.dba._queryLocalTripCurrentID()
        self.assertEqual(res, [1, 1], 'Current Trip was not set to complete')

if __name__ == '__main__':
    unittest.main()