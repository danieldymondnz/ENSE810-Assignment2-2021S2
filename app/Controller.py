from sense_emu import SenseHat
import threading
import time
import queue

import MatrixDriver
import DataCollection
import DBAgent

class Controller(object):

    LOCAL_DB_CONFIG = {
    "fileLocation": "test/testDB.db"
    }
    REMOTE_DB_CONFIG = {
        "host": "localhost",
        "user": "dbuser",
        "passwd": "l0ck3dR3alT!GHT:D",
        "db": "sdmms_db"
    }
    REGISTRATION = "TE5TNG"

    def __init__(self):
        
        threading.Thread.__init__(self)
        
        self._matrixDriver = MatrixDriver
        self._dataCollection = DataCollection
        self.dataQueue = dataQueue
        self.flushQueue = flushQueue
        self._senseHAT = SenseHat()
        
        # Setup the Database Agent
        self.dbDataQueue = queue.Queue()
        self.dbAgent = DBAgent(self.dbDataQueue, Controller.REGISTRATION, Controller.LOCAL_DB_CONFIG, Controller.REMOTE_DB_CONFIG)
        
        self.__dataUseDict = {}
        
        self.isRunning = True
        
    def run(self):

        # Start the Database Thread
        self.dbAgent.start()

        while self.isRunning:
            # collect data
            if DataCollection._DCDataQueue.qsize() > 0:
                self.__dataUseDict = self._DCDataQueue.get_nowait()
            
            # display data
            MatrixDriver._displayGraph(_senseHAT, dataUseDict["TEMPERATURE"], dataUseDict["HUMIDITY"])
            if dataUseDict["WARN_ACCELERATION"]:
                MatrixDriver._displayAccelerationWarning(self, _senseHAT, dataUseDict["ACCELERATION"])
            if dataUseDict["WARN_HUMIDITY"]:
                MatrixDriver._displayRHWarning(self, _senseHAT, dataUseDict["HUMIDITY"])
            if dataUseDict["WARN_SPEED"]:
                MatrixDriver._displaySpeedWarning(self, _senseHAT, dataUseDict["SPEED"])
            if dataUseDriver["WARN_TEMPERATURE"]:
                MatrixDriver._displayTempWarning(self, _senseHAT, dataUseDict["TEMPERATURE"])

            # transfer data to DBAgent

        # When Thread is being disposed, terminate other Threads
        self.dbAgent.terminate()
        
    def terminate(self):
        self.isRunning = False
        
    def _flushQueue(self):
        pass
        
    
