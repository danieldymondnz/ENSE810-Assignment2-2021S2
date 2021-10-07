'''
DBAgent
Database Agent, which uses connectivity to a remote database to record trips and
buffer data from a local SQLite to remote MySQL database.
Daniel Dymond 2021
'''

import datetime
import pymysql as remoteDB
import threading
import sqlite3 as localDB

class DBAgent(threading.Thread):

    # Set these flags for debugging in console
    ENABLE_VERBOSE = True

    # Constructor for this object
    def __init__(self, dataQueue, registration, localDBConfig, remoteDBConfig):
        
        # Call Thread Init Method
        threading.Thread.__init__(self)

        # Store references and information, create Running flag for Thread
        self._vehicleRegistration = registration
        self._dataQueue = dataQueue
        self._remoteConnectionChanged = False
        self._remoteIsAvailable = False
        self.isRunning = True

        # Extract localDBConfig Dictionary. If it fails, fall back to default
        try:
            self.localDBLocation = localDBConfig["fileLocation"]
        except:
            self.localDBLocation = "app/localDB.db"
            DBAgent.verbose("Error parsing local DB information, falling back to default.")

        # Perform Local DB Test to ensure location is valid
        try:
            self._connectLocalDB()
            self._localDBConn.cursor().execute("SELECT * FROM `TRIPS` ORDER BY UID DESC LIMIT 1")
            self._disconnectLocalDB()
        except:
            DBAgent.verbose("Error connecting to local database")
            raise

        # Extract remoteDBConfig Dictionary. If it fails, fall back to default
        try:
            self.remoteDBHost = remoteDBConfig["host"]
            self.remoteDBdb = remoteDBConfig["db"]
            self.remoteDBUser = remoteDBConfig["user"]
            self.remoteDBPasswd = remoteDBConfig["passwd"]
        except:
            self.remoteDBHost = ""
            self.remoteDBdb = ""
            self.remoteDBUser = ""
            self.remoteDBPasswd = ""
            DBAgent.verbose("Error parsing remote DB information. This agent will not be able to write inforamtion to remote.")
    
    ### LOCAL DATABASE : CONN METHODS ###

    # Connect to Local Database. Throws Exception on error.
    def _connectLocalDB(self):

        # Connect and attempt to get data from localDB
        try:
            self._localDBConn = localDB.connect(self.localDBLocation, uri=True)
        except localDB.Error as error:
            raise Exception("Local Database Error: %s" % (' '.join(error.args)))

    # Disconnects from Local Database.
    def _disconnectLocalDB(self):
        self._localDBConn.close()

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
    def _writeLocalDB(self, sqlQuery):
        
        # Write data to Local DB
        DBAgent.verbose("Local DB: Dict Write initiated")
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

    # Query information for the latest trip. Returns row matrix or None if no trips. Throws exception on error
    def _queryLocalLatestTrip(self):
   
        try:
            sqlQuery = "SELECT * FROM TRIPS ORDER BY UID DESC LIMIT 1"
            row = self._readLocalDB(sqlQuery)
        except Exception as ex:
            raise ex

        # Parse data and return
        if not(len(row) == 0):
            return row
        else:
            return None

    # Set the status of the latest trip as complete. Throws exception on error.
    def _setLocalTripCurrentComplete(self):

        sqlQuery = "UPDATE TRIPS SET TRIP_COMPLETE=1 WHERE UID=%s" % self._tripID

        # Connect to Local DB, Update Data, and Disconnect
        try:
            self._writeLocalDB(sqlQuery)
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Local Database Error: %s" % (' '.join(error.args)))

    # Query local database for oldest trip that needs to be synced. Return the trip, or None
    def _queryLocalTripToSync(self):
        
        try:
            sqlQuery = "SELECT * FROM TRIPS WHERE REMOTE_SYNC_COMPLETE=0 AND TRIP_COMPLETE=1 ORDER BY UID ASC LIMIT 1"
            row = self._readLocalDB(sqlQuery)
        except Exception as ex:
            raise ex

        # Parse data and return
        if not(len(row) == 0):
            return row
        else:
            return None

    # Establish a new Trip. Throws exception on error, if current trip is still not completed.
    def _createNewTrip(self):
        
        # Confirm current trip has been marked as complete
        currTrip = self._queryLocalLatestTrip()
        if not(currTrip == None):
            tripComp = currTrip[0][2]

            # If current trip not complete, throw exception
            if tripComp == 0:
                raise Exception("The current trip is still open. Complete trip before creating a new one.")

        sqlQuery = "INSERT INTO `TRIPS` (TRIP_COMPLETE, REMOTE_SYNC_COMPLETE, REMOTE_SYNC) VALUES (0, 0, 0)"
        self._writeLocalDB(sqlQuery)
        newTrip = self._queryLocalLatestTrip()
        self._tripID = newTrip[0][0]
        DBAgent.verbose("New Trip on Local DB #%s" % self._tripID)
        return self._tripID
            
    # Write a Dictionary containing raw data to the local DB
    def _writeDictToLocalDB(self, dictToWrite):
        
        # Generate the Local DB Query to write Data
        variables = (self._tripID, dictToWrite["ACCELERATION"], dictToWrite["HUMIDITY"], dictToWrite["SPEED"], dictToWrite["TEMPERATURE"])
        localDBQuery = "INSERT INTO `TRIP_DATA` (TRIP_ID, ACCELERATION, HUMIDITY, SPEED, TEMPERATURE) VALUES (%s, %s, %s, %s, %s)" % variables
        self._writeLocalDB(localDBQuery)
        self._setLocalTripWarningFlags(dictToWrite)

    # Update the trip with the warning flags
    def _setLocalTripWarningFlags(self, dictToWrite):

        acFl = int(dictToWrite["WARN_ACCELERATION"])
        huFl = int(dictToWrite["WARN_HUMIDITY"])
        spFl = int(dictToWrite["WARN_SPEED"])
        tpFl = int(dictToWrite["WARN_TEMPERATURE"])

        # If dictionary flags set, write to the trip attribute
        if acFl or huFl or spFl or tpFl:

            row = self._queryLocalLatestTrip();

            if row == None:
                return

            sqlQuery = "UPDATE TRIPS SET WARN_ACCELERATION=%s, WARN_HUMIDITY=%s, WARN_SPEED=%s, WARN_TEMPERATURE=%s WHERE UID=%s" % ((row[0][5] or acFl), (row[0][6] or huFl), (row[0][7] or spFl), (row[0][8] or tpFl), self._tripID)

            # Connect to Local DB, Update Data, and Disconnect
            try:
                self._writeLocalDB(sqlQuery)
            except Exception as exception:
                raise exception
            except localDB.Error as error:
                raise Exception("Local Database Error: %s" % (' '.join(error.args)))

    # Query local database for oldest record to syncGet the oldest local record from the DB. Return the data as a dictionary.
    def _queryLocalTripDataRecord(self, tripID):

        sqlQuery = "SELECT * FROM TRIP_DATA WHERE TRIP_ID = %s AND REMOTE_SYNCED=0 ORDER BY UID ASC LIMIT 1" % tripID
        print(sqlQuery)
        row = self._readLocalDB(sqlQuery)

        # Parse data and return
        if not(len(row) == 0):

            dictReturn = {
                "UID": row[0][0],
                "TIMESTAMP": row[0][1],
                "TRIP_ID": row[0][2],
                "REMOTE_SYNCED": row[0][3],
                "ACCELERATION": row[0][4],
                "HUMIDITY": row[0][5],
                "SPEED": row[0][6],
                "TEMPERATURE": row[0][7]
            }

            return dictReturn
        else:
            return None 

    # Update local database record to inidicate it has been written to the remote db
    def _setLocalTripDataRecordAsSynced(self, uid):
        
        sqlQuery = "UPDATE TRIP_DATA SET REMOTE_SYNCED=1 WHERE UID=%s" % uid

        # Connect to Local DB, Update Data, and Disconnect
        try:
            self._writeLocalDB(sqlQuery)
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Local Database Error: %s" % (' '.join(error.args)))

    # Update local database record to inidicate it has been written to the remote db
    def _setLocalTripSyncComplete(self, uid):
        
        sqlQuery = "UPDATE TRIPS SET REMOTE_SYNC_COMPLETE=1 WHERE UID=%s" % uid

        # Connect to Local DB, Update Data, and Disconnect
        try:
            self._writeLocalDB(sqlQuery)
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Local Database Error: %s" % (' '.join(error.args)))

    ### REMOTE DATABASE : COMM METHODS ###
    
    # Attempt to establish a connection with the remote database. Throws an exception on error     
    def _connectRemoteDB(self):

        # Connect and attempt to get data from remoteDB
        try:
            self._remoteDBConn = remoteDB.connect(host=self.remoteDBHost, user=self.remoteDBUser, passwd=self.remoteDBPasswd, db=self.remoteDBdb)
        except remoteDB.Error as error:
            raise Exception("Error connecting to Remote Database: %s" % (' '.join(error.args)))

    # Disconnects from Remote Database.
    def _disconnectRemoteDB(self):
        self._remoteDBConn.close()

    # Read information using SELECT query and return row(s). Throws Exception on error.
    def _readRemoteDB(self, sqlQuery):

        # Connect to Local DB, Retrieve Data, and Disconnect
        try:
            self._connectRemoteDB()
            cur = self._remoteDBConn.cursor()
            cur.execute(sqlQuery)
            self._remoteDBConn.commit()
            rows = cur.fetchall()
            self._disconnectRemoteDB()
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Error reading from Local Database: %s" % (' '.join(error.args)))

        # Return Data
        return rows

    # Write information using INSERT or UPDATE query. Throws Exception on error.
    def _writeRemoteDB(self, sqlQuery):
        # Write data to Local DB
        DBAgent.verbose("Remote DB: Dict Write initiated")
        DBAgent.verbose("Remote DB: %s" % sqlQuery)
        try:
            self._connectRemoteDB()
            self._remoteDBConn.cursor().execute(sqlQuery)
            self._remoteDBConn.commit()
            self._disconnectRemoteDB()
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Error writing to Local Database: %s" % (' '.join(error.args)))

    ### REMOTE DATABASE :  DATA METHODS ###

    # Write a trip record from the local database to the remote
    def _writeTripDataRecordToRemote(self, dictToWrite):
        
        # Parse the data from the dictionary
        registration = self._vehicleRegistration
        timestamp = datetime.datetime.strptime(dictToWrite["TIMESTAMP"], '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        local_uid = dictToWrite["UID"]
        trip_id = dictToWrite["TRIP_ID"]
        acceleration = dictToWrite["ACCELERATION"]
        humidity = dictToWrite["HUMIDITY"]
        speed = dictToWrite["SPEED"]
        temperature = dictToWrite["TEMPERATURE"]

        # With data parsed, construct SQL
        sqlQuery = "INSERT INTO TRIP_DATA (REGISTRATION, TIMESTAMP, LOCAL_UID, TRIP_ID, ACCELERATION, HUMIDITY, SPEED, TEMPERATURE) VALUES ('%s', '%s',%s, %s, %s, %s, %s, %s)" % (registration, timestamp, local_uid, trip_id, acceleration, humidity, speed, temperature)
        self._writeRemoteDB(sqlQuery)

    def _writeTripToRemote(self, tripToSync):

        # Parse data from Trip
        tripId = tripToSync[0][0]
        timeStamp = tripToSync[0][1]
        registration = self._vehicleRegistration
        tempWrn = tripToSync[0][5]
        huWrn = tripToSync[0][6]
        spWrn = tripToSync[0][7]
        accWrn = tripToSync[0][8]

        sqlQuery = "INSERT INTO `TRIPS` (`TRIP_ID`, `TRIP_TIMESTAMP`, `REGISTRATION`, `TEMP_WARN`, `HUMIDITY_WARN`, `SPEED_WARN`, `ACCEL_WARN`) VALUES (%s, '%s', '%s', %s, %s, %s, %s)" % (tripId, timeStamp, registration, tempWrn, huWrn, spWrn, accWrn)
        self._writeRemoteDB(sqlQuery)
        
        pass

    def _setRemoteTripSyncComplete(self, tripID):

        sqlQuery = "UPDATE TRIPS SET IS_SYNCED=1 WHERE REGISTRATION='%s' AND UID=%s" % (self._vehicleRegistration, tripID)

        # Connect to Local DB, Update Data, and Disconnect
        try:
            self._writeRemoteDB(sqlQuery)
        except Exception as exception:
            raise exception
        except localDB.Error as error:
            raise Exception("Local Database Error: %s" % (' '.join(error.args)))
        pass

    def _queryRemotePartiallySyncedTrips(self):

        sqlQuery = "SELECT * FROM `TRIPS` WHERE IS_SYNCED=0 AND REGISTRATION='%s' ORDER BY UID ASC LIMIT 1" % self._vehicleRegistration
        row = self._readRemoteDB(sqlQuery)

        if len(row) > 0:
            return int(row[0][2])
        else:
            return None

    def _bufferTripData(self):

        # Determine Trip to buffer. Check if any remaining on remote to sync, otherwise pull next oldest
        tripID = self._queryRemotePartiallySyncedTrips()

        # If none, find next on local and sync
        if tripID == None:
            tripToSync = self._queryLocalTripToSync()
            if tripToSync == None:
                return
            else:
                tripID = int(tripToSync[0][0])
                self._writeTripToRemote(tripToSync)

        # Find unbuffered record
        dictToBuffer = self._queryLocalTripDataRecord(tripID)
        
        # If no dict is returned, all trip data has been synced to remote. Mark this.
        if dictToBuffer == None:
            self._setLocalTripSyncComplete(tripID)
            self._setRemoteTripSyncComplete(tripID)
        
        # Otherwise, syncronise
        else:
            self._writeTripDataRecordToRemote(dictToBuffer)
            self._setLocalTripDataRecordAsSynced(int(dictToBuffer["UID"]))

    ### CONNECTION METHODS ###

    def setRemoteOffline(self):
        self._remoteIsAvailable = False
        self._remoteConnectionChanged = True

    def setRemoteOnline(self):
        self._remoteIsAvailable = True
        self._remoteConnectionChanged = True

    ### MAIN THREAD : INIT/CONFIG ###

    #Perform Initial Setup - Complete any incomplete trip (in case of power failure)
    def _initialSetup(self):
        
        # Determine current Trip Number
        currTrip = self._queryLocalLatestTrip()
        if currTrip == None:
            self._tripID = 0
            isComplete = 1
        else:
            self._tripID = currTrip[0][0]
            isComplete = currTrip[0][2]

        # If the current trip is still in progress, set to complete and increment tripID
        # The system may have been unexpectedly powered down during operation
        if not isComplete:
            self._setLocalTripCurrentComplete()

        # If the system is offline, then sync
        if not(self._remoteIsAvailable):
            self._createNewTrip()

    # Configures the Trip accordingly on connection change
    def _actionConnectionChange(self):

        # If the remote is available, terminate the current trip
        if self._remoteIsAvailable:
            self._setLocalTripCurrentComplete()

        # If the remote is unavailable, start a new trip
        else:
            self._createNewTrip()

        # With the change actioned, de-set the flag
        self._remoteConnectionChanged = False
    
    ## MAIN THREAD ##
    
    def run(self):

        # Perform the Initial Setup
        self._initialSetup()

        # Thread Loop - Continues until terminate() is publicly called
        while self.isRunning:

            # Pop a dictionary from the queue
            if self._dataQueue.qsize() > 0:
                dictToWrite = self._dataQueue.get_nowait()
            else:
                dictToWrite = None
            
            # If connectivity has just been lost or established, then start/end trip
            if self._remoteConnectionChanged:
                self._actionConnectionChange()

            # If Remote Online, ignore popped dictionary and buffer data to remote database
            if self._remoteIsAvailable:
                self._bufferTripData()

            # If Remote Offline, then write data to local database
            else:
                if not(dictToWrite == None):
                    self._writeDictToLocalDB(dictToWrite)
      
    # Terminates the DBAgent Thread
    def terminate(self):
        self.isRunning = False

    ### VERBOSE OUTPUT FOR DEBUGGING ###

    @staticmethod
    def verbose(textToPrint):
        if DBAgent.ENABLE_VERBOSE:
            print(textToPrint)
