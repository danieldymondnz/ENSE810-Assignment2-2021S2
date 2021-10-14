from sense_emu import SenseHat
import threading
import queue

from MatrixDriver import MatrixDriver
from DataCollection import DataCollection
from DBAgent import DBAgent

class Controller(threading.Thread):

    LOCAL_DB_CONFIG = {
    "fileLocation": "app/localDB.db"
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
        self.matrixQueue = queue.Queue()
        self._senseHAT = SenseHat()

        self._matrixDriver = MatrixDriver(self._senseHAT, self.matrixQueue)
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
                print("Pulled Data")
                self.__dataUseDict = self.dataQueue.get_nowait()

                # transfer data to MatrixDriver
                self.matrixQueue.put(self.__dataUseDict)
               
                #transfer data to DBAgent
                print("DB Agent Push")
                self.dbDataQueue.put(self.__dataUseDict)

        # When Thread is being disposed, terminate other Threads
        self.dbAgent.terminate()
        self._matrixDriver.terminate()
        self._dataCollection.terminate()
        
    def terminate(self):
        self.isRunning = False
        