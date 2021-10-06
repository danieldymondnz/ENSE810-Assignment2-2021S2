import threading
import sqlite3 as localDB
import pymysql as remoteDB

class DBAgent(threading.Thread):

    # Constants
    localDBLocation = "App/localDB.db"

    # Constructor for this object
    def __init__(self, dataQueue, localDBConfig, remoteDBConfig):
        self._dataQueue = dataQueue
        self.isRunning = True

        # Create connection to the Local DB
        self._connectToLocalDB(DBAgent.localDBLocation)

        pass
    
    # Attempt to establish a connection with the local database
    # Throws an exception on error
    def _connectToLocalDB(self, localDBFilePath):

        # Connect and attempt to get data from localDB
        try:
            self._localDBConn = localDB.connect(localDBFilePath)
            self._localDBConn.cursor().execute("SELECT * FROM `TRIPS`")
            self._localDBConn.commit()
        except localDB.Error as error:
            raise Exception("Error connection to Local Database: %s" % (' '.join(error.args)))

        # If connection is successful, then set flag
        self.localDBConnected = True
        
    # Attempt to establish a connection with the remote database
    # Throws an exception on error     
    def _connectToRemoteDB(self, address, database, username, password):

        # Connect and attempt to get data from remoteDB
        try:
            self._remoteDBConn = remoteDB.connect(host="localhost", user="dbuser", passwd="l0ck3dR3alT!GHT:D", db="week8DatabaseTest")
            self._remoteDBConn.cursor().execute("GET * FROM `TRIPS`")
            self._remoteDBConn.commit()
        except remoteDB.Error as error:
            raise Exception("Error connection to Remote Database: %s" % (' '.join(error.args)))

        # If connection is successful, then set flag
        self.remoteDBConnected = True

    # Query local database for oldest record that need to be synced
    # Return the ID, or -1 if none exist
    def _queryLocalTripStatus(self):

        sqlQuery = "SELECT * FROM TRIPS WHERE REMOTE_SYNC_COMPLETE=0 ORDER BY UID DESC LIMIT 1"
        row = self._localDBConn.cursor().execute(sqlQuery).fetchall()
        if not(len(row) == 0):
            return row[0][0]
        else:
            return -1






    @staticmethod    
    def _genLocalDBWriteQuery(dictToWrite, tripID):
        pass
    
    @staticmethod    
    def _genRemoteDBWriteQuery(dictToWrite):
        pass

    # Checks if Remote Database is available
    # For testing, this is a fixed variable
    def _remoteIsAvailable(self):
        return True

    # Write a dictionary to the Local Database    
    def _writeToLocalDB(self, dictToWrite):

        # Generate the Local DB Query to write Data
        localDBQuery = DBAgent._genLocalDBWriteQuery(dictToWrite, self.tripID)
        
        # Write data to Local DB
        try:
            self._localDBConn.cursor().execute(localDBQuery)
            self._localDBConn.commit()
        except localDB.Error as error:
            raise Exception("Error writing to Local Database: %s" % (' '.join(error.args)))
        
    # Transfer data from the Local DB to the Remote DB
    def _writeToRemoteDB(sqlQuery):
        pass
        
    def _getRemoteDBTripStatus():
        pass
        
    def _genNewTrip(dictToWrite):
        pass
        
    # Get the oldest local record from the DB
    def _getLocalDBRecord():
        
        # Write data to Local DB
        try:
            self._localDBConn.cursor().execute(localDBQuery)
            self._localDBConn.commit()
        except localDB.Error as error:
            raise Exception("Error writing to Local Database: %s" % (' '.join(error.args)))

        pass

    def run(self):

        while self.isRunning:

            # If connectivity has just been lost to Remote DB, start a new trip


            # If offline, then 
            






            continue

        pass
        
    # Terminates the DBAgent Thread
    def terminate(self):
        self.isRunning = False