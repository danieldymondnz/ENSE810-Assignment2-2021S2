import threading
import sqlite3 as localDB
import pymysql as remoteDB

class DBAgent(threading.Thread):

    ENABLE_VERBOSE_CONFIG = True
    ENABLE_VERBOSE_DBTRAN = False

    # Constructor for this object
    def __init__(self, dataQueue, registration, localDBConfig, remoteDBConfig):
        self._dataQueue = dataQueue
        self.isRunning = True

        # Extract localDBConfig Dictionary
        try:
            self.localDBLocation = localDBConfig["fileLocation"]
        except:
            self.localDBLocation = "App/localDB.db"
            DBAgent.verboseConf("Error parsing local DB information, falling back to default.")

        # Perform Local DB Test to ensure location is valid
        try:
            self._connectLocalDB()
            self._localDBConn.cursor().execute("SELECT * FROM `TRIPS` ORDER BY UID DESC LIMIT 1")
            self._disconnectLocalDB()
        except:
            DBAgent.verboseConf("Error connecting to local database")
            raise

        pass
    
    ### LOCAL DATABASE : CONN METHODS ###

    # Connect to Local Database. Throws Exception on error.
    def _connectLocalDB(self):

        # Connect and attempt to get data from localDB
        try:
            self._localDBConn = localDB.connect(self.localDBLocation, uri=True)
        except localDB.Error as error:
            raise Exception("Local Database Error: %s" % (' '.join(error.args)))

        # If connection is successful, then set flag
        self._localDBConnected = True

    # Disconnects from Local Database.
    def _disconnectLocalDB(self):
        self._localDBConn.close()
        self._localDBConnected = False

    # Returns wheter the Local Database is connected.
    def _isConnectedToLocalDB(self):
        return self.localDBConnected

    # Read information using SELECT query and return row(s). Throws Exception on error.
    def _readLocalDB(self, sqlQuery):

        # Connect to Local DB, Retrieve Data, and Disconnect
        try:
            self._connectLocalDB()
            rows = self._localDBConn.cursor().execute(sqlQuery).fetchall()
            self._disconnectLocalDB()
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Error reading from Local Database: %s" % (' '.join(error.args)))

        # Return Data
        return rows

    # Write information using INSERT or UPDATE query. Throws Exception on error.
    def _writeToLocalDB(self, sqlQuery):
        
        # Write data to Local DB
        try:
            self._connectLocalDB()
            self._localDBConn.cursor().execute(sqlQuery)
            self._localDBConn.commit()
            self._disconnectLocalDB()
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Error writing to Local Database: %s" % (' '.join(error.args)))

    ### LOCAL DATABASE : DATA METHODS ###

    # Query the status of the latest trip. Returns matrix: [TripID, TripComplete], or [-1, -1] if no trips. Throws exception on error
    def _queryLocalLatestTripStatus(self):

        sqlQuery = "SELECT * FROM TRIPS ORDER BY UID DESC LIMIT 1"
        row = self._readLocalDB(sqlQuery)

        # Parse data and return
        if not(len(row) == 0):
            return [row[0][0], row[0][2]]
        else:
            return [-1, -1]

    # Set the status of the latest trip as complete. Throws exception on error.
    def _setLocalTripCurrentComplete(self):

        sqlQuery = "UPDATE TRIPS SET TRIP_COMPLETE=1 WHERE UID=%s" % self._tripID

        # Connect to Local DB, Update Data, and Disconnect
        try:
            self._connectLocalDB()
            self._localDBConn.cursor().execute(sqlQuery)
            self._localDBConn.commit()
            self._disconnectLocalDB()
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Local Database Error: %s" % (' '.join(error.args)))

    # Query local database for oldest trip that needs to be synced. Return the ID, or -1 if none exist
    def _queryLocalTripSyncStatus(self):

        sqlQuery = "SELECT * FROM TRIPS WHERE REMOTE_SYNC_COMPLETE=0 ORDER BY UID DESC LIMIT 1"
        row = self._readLocalDB(sqlQuery)

        # Parse data and return
        if not(len(row) == 0):
            return row[0][0]
        else:
            return -1 

    # Establish a new Trip. Throws exception on error, if current trip is still not completed.
    def _createNewTrip(self):
        
        # Confirm current trip has been marked as complete
        _, tripComp = self._queryLocalLatestTripStatus()

        # If current trip not complete, throw exception
        if tripComp == 0:
            raise Exception("The current trip is still open. Complete trip before creating a new one.")
        
        # If complete, increment Trip ID and create new trip
        else:
            sqlQuery = "INSERT INTO `TRIPS` (TRIP_COMPLETE, REMOTE_SYNC_COMPLETE, REMOTE_SYNC) VALUES (0, 0, 0)"
            self._writeToLocalDB(sqlQuery)
            self._tripID, _ = self._queryLocalLatestTripStatus()
            
    # Write a Dictionary containing raw data to the local DB
    def _writeDictToLocalDB(self, dictToWrite):
        # Generate the Local DB Query to write Data
        variables = (self._tripID, dictToWrite["ACCELERATION"], dictToWrite["HUMIDITY"], dictToWrite["PRESSURE"], dictToWrite["SPEED"], dictToWrite["TEMP"])
        localDBQuery = "INSERT INTO `TRIP_DATA` (TRIP_ID, ACCELERATION, HUMIDITY, PRESSURE, SPEED, TEMP) VALUES (%s, %s, %s, %s, %s, %s)" % variables
        self._writeToLocalDB(localDBQuery)
        
    ### REMOTE DATABASE : COMM METHODS ###
    









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

    




    @staticmethod    
    def _genRemoteDBWriteQuery(dictToWrite):
        pass

    # Checks if Remote Database is available
    # For testing, this is a fixed variable
    def _remoteIsAvailable(self):
        return False



        
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

    
    ### MAIN THREAD : INIT/CONFIG ###

    #Perform Initial Setup for Thread
    #Closes any incomplete trip (in case of power failure), creates new trip locally
    def _initialSetup(self):
        
        # Determine current Trip Number
        self._tripID, isComplete = self._queryLocalLatestTripStatus()

        # If the current trip is still in progress, set to complete and increment tripID
        # The system may have been unexpectedly powered down during operation
        if not isComplete:
            self._setLocalTripCurrentComplete()

        # Determine Connectivity
        self.remoteConnected = self._remoteIsAvailable()

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

    ### VERBOSE OUTPUT FOR DEBUGGING ###

    @staticmethod
    def verboseConf(textToPrint):
        if DBAgent.ENABLE_VERBOSE_CONFIG:
            print(textToPrint)

    @staticmethod
    def verboseDBTran(textToPrint):
        if DBAgent.ENABLE_VERBOSE_DBTRAN:
            print(textToPrint)