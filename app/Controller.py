from sense_emu import SenseHat
import threading
import time
import queue

from MatrixDriver import MatrixDriver
from DataCollection import DataCollection
from DBAgent import DBAgent

class Controller(threading.Thread):

    LOCAL_DB_CONFIG = {
    "fileLocation": "app/testDB.db"
    }
    REMOTE_DB_CONFIG = {
        "host": "localhost",
        "user": "dbuser",
        "passwd": "l0ck3dR3alT!GHT:D",
        "db": "sdmms_db"
    }
    REGISTRATION = "SUC355"

    def __init__(self):
        
        threading.Thread.__init__(self)
        
        
        self.dataQueue = queue.Queue()
        self.flushQueue = queue.Queue()
        self._senseHAT = SenseHat()

        self._matrixDriver = MatrixDriver(self._senseHAT)
        self._dataCollection = DataCollection(self._senseHAT, self.dataQueue)
        
        # Setup the Database Agent
        self.dbDataQueue = queue.Queue()
        self.dbAgent = DBAgent(self.dbDataQueue, Controller.REGISTRATION, Controller.LOCAL_DB_CONFIG, Controller.REMOTE_DB_CONFIG)
        
        self.__dataUseDict = None
        
        self.isRunning = True
        
    def run(self):

        # Start the Database Thread
        self.dbAgent.start()
        self._matrixDriver.start()
        self._dataCollection.start()

        while self.isRunning:
            # collect data
            if self.dataQueue.qsize() > 0:
                self.__dataUseDict = self.dataQueue.get_nowait()
            
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
            if not(self.__dataUseDict == None):
                self.dbDataQueue.put(self.__dataUseDict)

        # When Thread is being disposed, terminate other Threads
        self.dbAgent.terminate()
        self._matrixDriver.terminate()
        self._dataCollection.terminate()
        
    def terminate(self):
        self.isRunning = False
        
    def _flushQueue(self):
        pass
        
    
