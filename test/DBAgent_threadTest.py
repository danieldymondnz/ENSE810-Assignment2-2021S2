import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir) + '/app'
sys.path.append(parentdir)
print(parentdir)

from DBAgent import DBAgent
import csv
import queue
import time

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

# Create Queue of Test Data
testQueue = queue.Queue()
with open(TEST_DATA_CSV) as csv_file:
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
            testQueue.put(dictToPlace)

        line_count += 1

    print(testQueue.qsize())

# Create the DBAgent, but do not start as thread
try:
    dba = DBAgent(testQueue, REGISTRATION, LOCAL_DB_CONFIG, REMOTE_DB_CONFIG)
    dba.start()
    time.sleep(10)
    dba.setRemoteOnline()
    time.sleep(10)
finally:
    dba.terminate()