import sqlite3 as localDB

class DBAgent(threading.Thread):

    # Constant Variables


    #
    self._dataQueue = None
    self._localDBPath = None
    self._localDBConn = None


    # Constructor for this object
    def __init__(self, dataQueue):
        self._dataQueue = dataQueue
        self._localDBPath = None
        pass
        
    def run(self):
        pass
        
    def terminate(self):
        pass
        
    def _connectToLocalDB(localDBFilePath):
        self._localDBConn = localDB.connect('localDB.db')
        pass
        
    def _connectToRemoteDB(address, database, username, password):
        pass
        
    def checkRemoteConnectivity():
        pass
        
    def _genLocalDBWriteQuery(dictToWrite):
        pass
        
    def _genRemoteDBWriteQuery(dictToWrite):
        pass
        
    def _writeToLocalDB(sqlQuery):
        pass
        
    def _writeToRemoteDB(sqlQuery):
        pass
        
    def _getRemoteDBTripStatus():
        pass
        
    def _genNewTrip(dictToWrite):
        pass
        
    def _getLocalDBRecord():
        pass
