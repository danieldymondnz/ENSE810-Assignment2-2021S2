from sense_emu import SenseHat
import threading
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
                self._matrixDriver._displayGraph(self._senseHAT, self.dataUseDict["TEMPERATURE"], self.dataUseDict["HUMIDITY"])
                if self.dataUseDict["WARN_ACCELERATION"]:
                    self._matrixDriver._displayAccelerationWarning(self, self._senseHAT, self.dataUseDict["ACCELERATION"])
                if self.dataUseDict["WARN_HUMIDITY"]:
                    self._matrixDriver._displayRHWarning(self, self._senseHAT, self.dataUseDict["HUMIDITY"])
                if self.dataUseDict["WARN_SPEED"]:
                    self._matrixDriver._displaySpeedWarning(self, self._senseHAT, self.dataUseDict["SPEED"])
                if self.dataUseDriver["WARN_TEMPERATURE"]:
                    self._matrixDriver._displayTempWarning(self, self._senseHAT, self.dataUseDict["TEMPERATURE"])


            self._senseHAT.set_pixels([self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Red, self.Red, self.Red,
                    self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green, self.Green,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange,
                    self.Blue, self.Blue, self.Green, self.Green, self.Green, self.Green, self.Orange, self.Orange])

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
