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

    LOCAL_DB_CONFIG = {
        "fileLocation": "test/testDB.db"
    }
    REMOTE_DB_CONFIG = {
        "host": "localhost",
        "user": "dbuser",
        "passwd": "l0ck3dR3alT!GHT:D",
        "db": "sdmms_db"
    }
    TEST_DATA_CSV = "test/testData.csv"
    REGISTRATION = "TE5TNG"

    def setUp(self):

        # Create Queue of Test Data
        with open(DBAgent_test.TEST_DATA_CSV) as csv_file:
            self.testQueue = queue.Queue()
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    pass
                else:
                    dictToPlace = {
                        "ACCELERATION": row[0],
                        "HUMIDITY": row[1],
                        "SPEED": row[2],
                        "TEMPERATURE": row[3],
                        "WARN_ACCELERATION": row[4],
                        "WARN_HUMIDITY": row[5],
                        "WARN_SPEED": row[6],
                        "WARN_TEMPERATURE": row[7]
                    }
                    self.testQueue.put(dictToPlace)

                line_count += 1

        # Create the DBAgent, but do not start as thread
        self.dba = DBAgent(self.testQueue, DBAgent_test.REGISTRATION, DBAgent_test.LOCAL_DB_CONFIG, DBAgent_test.REMOTE_DB_CONFIG)
        self.dba._initialSetup()

    def test_queryLocalTripSyncStatus(self):
        res = self.dba._queryLocalTripSyncStatus()
        self.assertGreater(res, 0, 'No valid UID could be obtained')

    def test_createNewTrip(self):
        currTripID, tripComp = self.dba._queryLocalLatestTripStatus()
        if tripComp == 0:
            self.dba._setLocalTripComplete()
        newTripID = self.dba._createNewTrip()
        self.assertEqual(currTripID + 1, newTripID, 'A new trip was not created as expected.')

    def test_writeDictToLocalDB(self):
        self.dba._writeDictToLocalDB(self.testQueue.get_nowait())

    def test_queryLocalTripDataRecord(self):
        dictReturned = self.dba._queryLocalTripDataRecord(1)
        self.assertIsInstance(dictReturned, dict, "A dictionary was not returned.")

    def test_setLocalTripDataRecordAsSynced(self):
        dictReturned = self.dba._queryLocalTripDataRecord(1)
        oldId = int(dictReturned["UID"])
        self.dba._setLocalTripDataRecordAsSynced(oldId)
        dictReturned = self.dba._queryLocalTripDataRecord(1)
        newId = int(dictReturned["UID"])
        self.assertNotEqual(oldId, newId, "The local database was unable to set a record as synced.")

    ### REMOTE DB ###
    def test_connectRemoteDB(self):
        self.dba._connectRemoteDB()
        boolean = self.dba._isConnectedToRemoteDB()
        self.dba._disconnectRemoteDB()
        self.assertEqual(True, boolean, "The database did not connect.")


if __name__ == '__main__':
    unittest.main()