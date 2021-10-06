import threading
import sqlite3 as localDB
import pymysql as remoteDB

class DBAgent(threading.Thread):

    # Constructor for this object
    def __init__(self, dataQueue, localDBConfig, remoteDBConfig):
        self._dataQueue = dataQueue
        self.isRunning = True

        # Extract Local DB Configuration and connect to the Local DB
        try:
            self.localDBLocation = localDBConfig["fileLocation"]
        except:
            self.localDBLocation = "App/localDB.db"
            raise Exception("Error parsing local DB information, falling back to default.")
        

        pass
    
    # Attempt to establish a connection with the local database
    # Throws an exception on error
    def _connectToLocalDB(self, localDBFilePath):

        # Connect and attempt to get data from localDB
        try:
            self._localDBConn = localDB.connect(localDBFilePath, uri=True)
            self._localDBConn.cursor().execute("SELECT * FROM `TRIPS`")
        except localDB.Error as error:
            raise Exception("Error connection to Local Database: %s" % (' '.join(error.args)))

        # If connection is successful, then set flag
        self.localDBConnected = True

    # Safely disconnect from local DB
    def _disConnectLocalDB(self):
        self._localDBConn.close()

    # Query local database for oldest record that need to be synced
    # Return the ID, or -1 if none exist
    def _queryLocalTripSyncStatus(self):

        sqlQuery = "SELECT * FROM TRIPS WHERE REMOTE_SYNC_COMPLETE=0 ORDER BY UID DESC LIMIT 1"
        row = self._localDBConn.cursor().execute(sqlQuery).fetchall()
        if not(len(row) == 0):
            return row[0][0]
        else:
            return -1

    # Query local database for current trip ID
    # Return row vector [current trip, is trip completed]
    def _queryLocalTripCurrentID(self):

        sqlQuery = "SELECT * FROM TRIPS ORDER BY UID DESC LIMIT 1"
        row = self._localDBConn.cursor().execute(sqlQuery).fetchall()
        if not(len(row) == 0):
            return [row[0][0], row[0][2]]
        else:
            return [-1, -1]

    # Mark the current trip as completed
    def _setLocalTripCurrentComplete(self):

        sqlQuery = "UPDATE TRIPS SET TRIP_COMPLETE=1 WHERE UID=%s" % self.tripID
        self._localDBConn.cursor().execute(sqlQuery)
        self._localDBConn.commit()

    # Establish new Trip
    def _createNewTrip(self):
        
        # Confirm current trip has been marked as complete
        _, tripComp = self._queryLocalTripCurrentID()

        # If complete, increment Trip ID and create new trip
        if tripComp == 1:
            sqlQuery = "INSERT INTO `TRIPS` (TRIP_COMPLETE, REMOTE_SYNC_COMPLETE, REMOTE_SYNC) VALUES (0, 0, 0)"
            self.tripID, _ = self._queryLocalTripCurrentID()
        else:
            raise Exception("The current trip is still open. Complete trip before creating a new one.")

        
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

    

    


    # Generate an Insert Query for the local database
    @staticmethod    
    def _genLocalDBWriteQuery(dictToWrite, tripID):

        variables = (tripID, dictToWrite["ACCELERATION"], dictToWrite["HUMIDITY"], dictToWrite["PRESSURE"], dictToWrite["SPEED"], dictToWrite["TEMP"])
        return "INSERT INTO `TRIP_DATA` (TRIP_ID, ACCELERATION, HUMIDITY, PRESSURE, SPEED, TEMP) VALUES (%s, %s, %s, %s, %s, %s)" % variables

    




    @staticmethod    
    def _genRemoteDBWriteQuery(dictToWrite):
        pass

    # Checks if Remote Database is available
    # For testing, this is a fixed variable
    def _remoteIsAvailable(self):
        return False

    def _writeDictToLocalDB(self, dictToWrite):
        # Generate the Local DB Query to write Data
        localDBQuery = DBAgent._genLocalDBWriteQuery(dictToWrite, self.tripID)
        self._writeToLocalDB(localDBQuery)
        

    # Write a dictionary to the Local Database    
    def _writeToLocalDB(self, localDBQuery):
        
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
        pass

    # Perform Initial Setup
    def _initialSetup(self):
        
        # Connect to Local DB, and Determine current Trip Number
        self._connectToLocalDB(self.localDBLocation)
        self.tripID, isComplete = self._queryLocalTripCurrentID()

        # If the current trip is still in progress, set to complete and increment tripID
        # The system may have been unexpectedly powered down during operation
        if not isComplete:
            self._setLocalTripCurrentComplete()
            self.tripID += 1

        # Determine Connectivity
        self.remoteConnected = self._remoteIsAvailable()

    def _cleanup(self):
        
        # Perform connection cleanup
        self._localDBConn.close()


    ## MAIN THREAD ##

    def run(self):

        # Perform the Initial Setup
        self._initialSetup()

        while self.isRunning:

            # Pop a dictionary from the queue
            dictToWrite = self._dataQueue.get_nowait()
            
            # If connectivity has just been lost to Remote DB, start a new trip


            if self._remoteIsAvailable():
                
                continue

            # If offline, then write data to local database
            else:
                self._writeDictToLocalDB(dictToWrite)

        # When the thread is terminated, close connection
        self._cleanup()
        
        
    # Terminates the DBAgent Thread
    def terminate(self):
        self.isRunning = False