import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir) + '/app'
sys.path.append(parentdir)
print(parentdir)

from DBAgent import DBAgent
import csv
import queue
import unittest


class DBAgent_test(unittest.TestCase):

    localDBConfig = {
        "fileLocation": "test/testDB.db"
    }
    TEST_DATA_CSV = "testData.csv"
    REGISTRATION = "TE5TNG"

    def setUp(self):

        # Create Queue of Test Data
        self.testQueue = queue.Queue()
        csv_reader = csv.reader(DBAgent_test.TEST_DATA_CSV, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                continue
            else:
                dictToPlace = {
                    "ACCELERATION": row[0],
                    "HUMIDITY": row[1],
                    "PRESSURE": row[2],
                    "SPEED": row[3],
                    "TEMPERATURE": row[4]
                }
                self.testQueue.put(dictToPlace)

            line_count += 1

        # Create the DBAgent, but do not start as thread
        self.dba = DBAgent(self.testQueue, DBAgent_test.REGISTRATION, DBAgent_test.localDBConfig, 0)
        self.dba._initialSetup()

    def test_queryLocalTripSyncStatus(self):
        res = self.dba._queryLocalTripSyncStatus()
        self.assertGreater(res, 0, 'No valid UID could be obtained')

if __name__ == '__main__':
    unittest.main()